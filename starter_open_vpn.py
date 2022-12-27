import os
import sys
import time
import re
import subprocess
# from datetime import date


VPN_SERVER_IP='137.184.105.94' # ACME VPN IP
IP_ADDRESS = "10.0.0.99"          # IP de la comunicación VPN

def main():

    # print("Connecting to chip")
    os.system("ppp -c")
    # print("connecting VPN")

    # Do it every reboot (we'll put it in /etc/rc.local)
    os.system("") # ejecutamos el comando para el openvpn


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