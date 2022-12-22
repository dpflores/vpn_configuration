#
# Copyright (C) 2016-2022 Lin Song <linsongui@gmail.com>
#
# This work is licensed under the Creative Commons Attribution-ShareAlike 3.0
# Unported License: http://creativecommons.org/licenses/by-sa/3.0/
#
# Attribution required: please include my name in any derivative and let me
# know how you have improved it!

FROM debian:bullseye-slim

RUN apt-get -y update \
    && DEBIAN_FRONTEND=noninteractive \
    && apt-get install strongswan xl2tpd net-tools
 

COPY ./run.sh /opt/src/run.sh
RUN chmod 755 /opt/src/run.sh
EXPOSE 500/udp 4500/udp
# CMD ["/opt/src/run.sh"]

RUN useradd --create-home --shell /bin/bash axotec_user && echo "axotec_user:axotec" | chpasswd && adduser axotec_user sudo
WORKDIR /home/axotec_user

USER axotec_user





CMD ["bash"]
