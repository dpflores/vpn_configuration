import os
import sys
import time
import re
import subprocess
# from datetime import date



IP_ADDRESS = "www.google.com"     # VERIFICAR QUE SEA ESTÁTICO



def main():


    while True:
        result = subprocess.run(["ping", "-c", "1", IP_ADDRESS], stdout=subprocess.PIPE)
        if result.returncode == 0:
            os.system("echo La conexión está activa")
            # print(f"La conexión con {IP_ADDRESS} está activa")
            pass
        else:
            os.system("echo La conexión se ha perdido")
            os.system("reboot")
            # print(f"La conexión con {IP_ADDRESS} NO está activa")
            sys.exit(1)
        time.sleep(180)


if __name__ == '__main__':
    try:
        main()

    except:
        sys.exit(1)
