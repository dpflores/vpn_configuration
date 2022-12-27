import os
import sys
import time
import re
# from datetime import date

import socket

VPN_SERVER_IP='137.184.105.94' # ACME VPN IP
IP_COMM = "10.0.0.99"          # IP de la comunicación VPN

def main():

    # print("Connecting to chip")
    os.system("ppp -c")
    # print("connecting VPN")

    # Do it every reboot (we'll put it in /etc/rc.local)
    os.system("") # ejecutamos el comando para el openvpn


    while True:
        try:
            socket.gethostbyname(IP_COMM)
            # Si llegamos aquí, significa que tenemos conexión a Internet
            conectado = True
            

        except socket.gaierror:
            # Si llegamos aquí, significa que no tenemos conexión a Internet
            conectado = False   
            sys.exit(1)
        print(f"Connected: {conectado}")
        time.sleep(5)
        


if __name__ == '__main__':
    try:
        main()

    except:
        sys.exit(1)