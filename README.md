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







# Creacion de un servicio en linux

Para crear un servicio con systemd, primero debes crear un archivo de configuración para el servicio. Este archivo debe tener un nombre que termine en .service y debe estar ubicado en el directorio /etc/systemd/system. El archivo debe contener información sobre el servicio, como su nombre, el comando que se debe ejecutar para iniciar el servicio, y las dependencias del servicio.

```
cd /etc/systemd/system
touch vpn_acme.service
nano vpn_acme.service
```


```
[Unit]
Description=Mi servicio mqtt
After=multi-user.target

[Service]

Type=simple

ExecStart=/home/del/Del/Programming/python/python_mqtt/venv-python_mqtt/bin/python /home/del/Del/Programming/python/python_mqtt/main.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

systemctl enable vpn_acme.service

systemctl status vpn_acme.service

python3 vpn_configuration/starter_vpn_acme.py

