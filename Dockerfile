FROM balenalib/raspberry-pi-debian:stretch-build
RUN useradd --create-home --shell /bin/bash axotec_user && echo "axotec_user:axotec" | chpasswd && adduser axotec_user sudo
WORKDIR /home/axotec_user

USER axotec_user

RUN apt-get update
RUN apt-get install strongswan xl2tpd net-tools



CMD ["bash"]
