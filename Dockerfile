
FROM ubuntu:focal

RUN apt-get update --privileged

RUN apt-get install git -y
RUN apt-get install python3.8 python3.8-dev -y

RUN printf '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d

RUN apt-get install wget -y


RUN apt-get install strongswan xl2tpd net-tools -y


RUN VPN_SERVER_IP='137.184.105.94'
RUN VPN_IPSEC_PSK='Mikrotik123*'
RUN VPN_USER='PROYECTOS2'
RUN VPN_PASSWORD='121383Loco!'


RUN cat > /etc/ipsec.conf <<EOF \
# ipsec.conf - strongSwan IPsec configuration file \
conn myvpn \
  auto=add \
  keyexchange=ikev1\
  authby=secret\
  type=transport\
  left=%defaultroute\
  leftprotoport=17/1701\
  rightprotoport=17/1701\
  right=$VPN_SERVER_IP\
  ike=aes128-sha1-modp2048\
  esp=aes128-sha1\
EOF

RUN cat > /etc/ipsec.secrets <<EOF\
: PSK "$VPN_IPSEC_PSK"\
EOF

RUN chmod 600 /etc/ipsec.secrets



RUN cat > /etc/xl2tpd/xl2tpd.conf <<EOF\
[lac myvpn]\
lns = $VPN_SERVER_IP\
ppp debug = yes\
pppoptfile = /etc/ppp/options.l2tpd.client\
length bit = yes\
EOF

RUN cat > /etc/ppp/options.l2tpd.client <<EOF\
ipcp-accept-local\
ipcp-accept-remote\
refuse-eap\
require-chap\
noccp\
noauth\
mtu 1280\
mru 1280\
noipdefault\
defaultroute\
usepeerdns\
connect-delay 5000\
name "$VPN_USER"\
password "$VPN_PASSWORD"\
EOF

RUN chmod 600 /etc/ppp/options.l2tpd.client

RUN mkdir -p /var/run/xl2tpd

RUN touch /var/run/xl2tpd/l2tp-control

COPY --chown=root:root . /home/applications/vpn_configuration

RUN /usr/bin/python3 

CMD ["python3","/home/applications/vpn_configuration/starter_vpn.py"]

# CMD ["bash"]
