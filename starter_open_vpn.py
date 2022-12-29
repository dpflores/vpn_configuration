import os
import sys
import time
import re
import subprocess
# from datetime import date


IP_ADDRESS = "10.20.0.31"          # IP de la comunicación VPN

def main():

    # print("Connecting to chip")
    os.system("pppd call gprs")
    # print("connecting VPN")

    # Do it every reboot (we'll put it in /etc/rc.local)
    os.system("openvpn --config /root/userKomatsuLE200_01_Axotec.ovpn") # ejecutamos el comando para el openvpn


    while True:
        result = subprocess.run(["ping", "-c", "1", IP_ADDRESS], stdout=subprocess.PIPE)
        if result.returncode == 0:
            os.system("echo La conexión está activa")
        else:
            os.system("echo La conexión se ha perdido")
            sys.exit(1)
        time.sleep(5)
        


if __name__ == '__main__':
    try:
        main()

    except:
        sys.exit(1)