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
    os.system("echo Conexion al chip realizado")
    # print("connecting VPN")

    time.sleep(10)

    # Do it every reboot (we'll put it in /etc/rc.local)
    os.system("openvpn --daemon --config /root/userKomatsuLE200_01_Axotec.ovpn") # ejecutamos el comando para el openvpn
    # el daemon es para que se ejecute en segundo plano y no muestre los logs


    while True:
        result = subprocess.run(["ping", "-c", "1", IP_ADDRESS], stdout=subprocess.PIPE)
        if result.returncode == 0:
            os.system("echo La conexión está activa")
        else:
            os.system("echo La conexión se ha perdido")
            sys.exit(1)
        time.sleep(10)
        


if __name__ == '__main__':
    try:
        main()

    except:
        sys.exit(1)