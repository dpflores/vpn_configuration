import os
import sys
import time
import re
import subprocess
# from datetime import date


IP_ADDRESS = "10.20.0.31"          # IP de la comunicación VPN

def main():

    # print("Connecting to chip")
    os.system("ppp -c")
    # print("connecting VPN")

    # Do it every reboot (we'll put it in /etc/rc.local)
    os.system("openvpn3 session-start --config /root/userKomatsuLE200_01_Axotec.ovpn") # ejecutamos el comando para el openvpn


    while True:
        result = subprocess.run(["ping", "-c", "1", IP_ADDRESS], stdout=subprocess.PIPE)
        if result.returncode == 0:
            print(f"La conexión con {IP_ADDRESS} está activa")
        else:
            print(f"La conexión con {IP_ADDRESS} NO está activa")
            sys.exit(1)
        time.sleep(5)
        


if __name__ == '__main__':
    try:
        main()

    except:
        sys.exit(1)