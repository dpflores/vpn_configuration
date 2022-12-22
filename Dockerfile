#
# Copyright (C) 2016-2022 Lin Song <linsongui@gmail.com>
#
# This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
# Unported License: http://creativecommons.org/licenses/by-sa/3.0/
#
# Attribution required: please include my name in any derivative and let me
# know how you have improved it!

FROM debian:bullseye-slim

ENV SWAN_VER 4.9
WORKDIR /opt/src

RUN apt-get -yqq update \
    && DEBIAN_FRONTEND=noninteractive \
       apt-get -yqq --no-install-recommends install \
         wget dnsutils openssl ca-certificates kmod iproute2 \
         gawk net-tools iptables bsdmainutils libcurl3-nss \
         libnss3-tools libevent-dev uuid-runtime xl2tpd \
         libnss3-dev libnspr4-dev pkg-config libpam0g-dev \
         libcap-ng-dev libcap-ng-utils libselinux1-dev \
         libcurl4-nss-dev flex bison gcc make \
    && wget -t 3 -T 30 -nv -O libreswan.tar.gz "https://github.com/libreswan/libreswan/archive/v${SWAN_VER}.tar.gz" \
    || wget -t 3 -T 30 -nv -O libreswan.tar.gz "https://download.libreswan.org/libreswan-${SWAN_VER}.tar.gz" \
    && tar xzf libreswan.tar.gz \
    && rm -f libreswan.tar.gz \
    && cd "libreswan-${SWAN_VER}" \
    && printf 'WERROR_CFLAGS=-w -s\nUSE_DNSSEC=false\nUSE_SYSTEMD_WATCHDOG=false\n' > Makefile.inc.local \
    && printf 'USE_DH2=true\nUSE_NSS_KDF=false\nFINALNSSDIR=/etc/ipsec.d\n' >> Makefile.inc.local \
    && make -s base \
    && make -s install-base \
    && cd /opt/src \
    && rm -rf "/opt/src/libreswan-${SWAN_VER}" \
    && apt-get -yqq remove \
         libnss3-dev libnspr4-dev pkg-config libpam0g-dev \
         libcap-ng-dev libcap-ng-utils libselinux1-dev \
         libcurl4-nss-dev flex bison gcc make \
    && apt-get -yqq autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/log/* \
    && update-alternatives --set iptables /usr/sbin/iptables-legacy

RUN wget -t 3 -T 30 -nv -O /opt/src/ikev2.sh https://github.com/hwdsl2/setup-ipsec-vpn/raw/fec1b7c7a22e037a69a1da9c68527f5d832dc3b5/extras/ikev2setup.sh \
    && chmod +x /opt/src/ikev2.sh \
    && ln -s /opt/src/ikev2.sh /usr/bin

COPY ./run.sh /opt/src/run.sh
RUN chmod 755 /opt/src/run.sh
EXPOSE 500/udp 4500/udp
# CMD ["/opt/src/run.sh"]

RUN useradd --create-home --shell /bin/bash axotec_user && echo "axotec_user:axotec" | chpasswd && adduser axotec_user sudo
WORKDIR /home/axotec_user

USER axotec_user





CMD ["bash"]
