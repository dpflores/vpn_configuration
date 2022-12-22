import os
import sys
import time
from datetime import date

VPN_SERVER_IP='137.184.105.94' #ACME VPN IP

def main():

    # print("Connecting to chip")
    os.system("ppp -c")
    # print("connecting VPN")

    # Do it every reboot (we'll put it in /etc/rc.local)
    os.system("mkdir -p /var/run/xl2tpd")
    os.system("touch /var/run/xl2tpd/l2tp-control")

    os.system("service strongswan restart")
    os.system("ipsec restart")
    os.system("service xl2tpd restart")

    os.system("ipsec up myvpn")
    os.system("echo \"c myvpn\" > /var/run/xl2tpd/l2tp-control")

    # Getting chip IP
    # output = os.popen("ifconfig ppp0").read()  chio
    output = os.popen("ip route").read() 
    import re

    pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

    match = re.search(pattern, output)
    
    ip_local = match.group()

    print("IP del chip:", ip_local)

    
    os.system(f"route add {VPN_SERVER_IP} gw {ip_local}")
    
    time.sleep(5)
    # os.system("")
    
    # os.system("r")

    os.system("route add default dev ppp0")
    # os.system("route add default dev ppp1")
    time.sleep(5)
    os.system("wget -qO- http://ipv4.icanhazip.com; echo")


if __name__ == '__main__':
    main()