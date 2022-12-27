import os
import sys
import time
import re
import subprocess
# from datetime import date


VPN_SERVER_IP='137.184.105.94' # ACME VPN IP
IP_ADDRESS = "10.0.0.99"  

CONNECTION = "wifi"     # "chip" para datos moviles o "wifi" para la conexion a un router

def get_ip_string(text):
    pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

    match = re.search(pattern, text)
    
    return match.group()

def main():

    # print("Connecting to chip")
    if CONNECTION=="chip":
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
    
    if CONNECTION == "chip":
        output = os.popen("ifconfig ppp0").read()   #chip
    
    if CONNECTION == "wifi":
        output = os.popen("ip route").read()      #network   
    
    
    ip_local = get_ip_string(output)

    print("IP del chip:", ip_local)

    
    os.system(f"route add {VPN_SERVER_IP} gw {ip_local}")
    
    time.sleep(1)
   

    if CONNECTION == "wifi":
        os.system("route add default dev ppp0")
    
    if CONNECTION == "chip":
        os.system("route add default dev ppp1")

    time.sleep(2)
    vpn_ip_result = os.system("wget -qO- http://ipv4.icanhazip.com; echo")
    vpn_ip_result_raw = os.popen("wget -qO- http://ipv4.icanhazip.com; echo").read()
    
    vpn_ip_result = get_ip_string(vpn_ip_result_raw)


    if vpn_ip_result != VPN_SERVER_IP:
        sys.exit(1)
    

    while True:
        result = subprocess.run(["ping", "-c", "1", IP_ADDRESS], stdout=subprocess.PIPE)
        if result.returncode == 0:
            print(f"La conexión con {IP_ADDRESS} está activa")
            pass
        else:
            print(f"La conexión con {IP_ADDRESS} NO está activa")
            sys.exit(1)
        time.sleep(5)


if __name__ == '__main__':
    try:
        main()

    except:
        sys.exit(1)