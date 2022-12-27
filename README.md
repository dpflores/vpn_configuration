install docker (version = )
https://docs.docker.com/engine/install/debian/



docker run --name vpn_container --restart=always --privileged --network host -it vpn_image 

docker run --name vpn_container --restart=always --privileged --network host -it ubuntu:focal


ubuntu:focal

apt-get update

apt-get install git -y
apt-get install python3.8 python3.8-dev -y


printf '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d

apt-get install wget -y


apt-get install strongswan xl2tpd net-tools -y



VPN_SERVER_IP='137.184.105.94'
VPN_IPSEC_PSK='Mikrotik123*'
VPN_USER='PROYECTOS4'
VPN_PASSWORD='121383Loco!'






route add 137.184.105.94 gw 192.168.88.1

route add default dev ppp0

wget -qO- http://ipv4.icanhazip.com; echo







