import os
import sys
from datetime import date

VPN_SERVER_IP='137.184.105.94' #ACME VPN IP

def main():
	print("Configuring VPN...")
	print("1. Ensure that the device has a connection to the Internet\n2. Check if the date is correct (current date: " + str(date.today()) + ").")
	print("The official install script will be started now. Unless you have any other requirements, we recommend to answer all following questions with y (yes).")
	res = input("Would you like to proceed? [y/N] ")
	if not (res == "y" or res == "Y"):
		print("Abort.")
		sys.exit(1)

	os.system("apt-get update")
	os.system("apt-get install strongswan xl2tpd net-tools")
	os.system("apt-get install strongswan xl2tpd net-tools")	

	os.system("VPN_SERVER_IP='137.184.105.94'")
	os.system("VPN_IPSEC_PSK='Mikrotik123*'")
	os.system("VPN_USER='ACMCel'")
	os.system("VPN_PASSWORD='121383Loco!'")
	os.system("cat > /etc/ipsec.conf <<EOF\n# ipsec.conf - strongSwan IPsec configuration file \nconn myvpn \n  auto=add \n  keyexchange=ikev1 \n  authby=secret \n  type=transport \n  left=%defaultroute \n  leftprotoport=17/1701 \n  rightprotoport=17/1701 \n  right=$VPN_SERVER_IP \n  ike=aes128-sha1-modp2048 \n  esp=aes128-sha1\nEOF")
	os.system("cat > /etc/ipsec.secrets <<EOF\n: PSK \"$VPN_IPSEC_PSK\"\nEOF")
	os.system("chmod 600 /etc/ipsec.secrets")
	os.system("cat > /etc/xl2tpd/xl2tpd.conf <<EOF\n[lac myvpn]\nlns = $VPN_SERVER_IP \nppp debug = yes \npppoptfile = /etc/ppp/options.l2tpd.client \nlength bit = yes\nEOF")

	os.system("cat > /etc/ppp/options.l2tpd.client <<EOF\nipcp-accept-local\nipcp-accept-remote\nrefuse-eap\nrequire-chap\nnoccp\nnoauth\nmtu 1280\nmru 1280\nnoipdefault\ndefaultroute\nusepeerdns\nconnect-delay 5000\nname \"$VPN_USER\"\npassword \"$VPN_PASSWORD\"\nEOF")
	os.system("chmod 600 /etc/ppp/options.l2tpd.client")

	print("VPN client setup complete")

	print("connecting VPN")

	# Do it every reboot (we'll put it in /etc/rc.local)
	os.system("mkdir -p /var/run/xl2tpd")
	os.system("touch /var/run/xl2tpd/l2tp-control")

	os.system("service strongswan restart")
	os.system("ipsec restart")
	os.system("service xl2tpd restart")

	os.system("ipsec up myvpn")
	os.system("echo \"c myvpn\" > /var/run/xl2tpd/l2tp-control")

	output = os.popen("ip route").read()
	import re

	pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

	match = re.search(pattern, output)
	if match:
		ip_local = match.group()

	os.system(f"route add {VPN_SERVER_IP} gw {ip_local}")

	os.system("route add default dev ppp0")
	os.system("wget -qO- http://ipv4.icanhazip.com; echo")

	# Creamos el archivo que se ejecutará cada vez

	os.system("cat > /etc/init.d/startup_script <<EOF\n /usr/bin/python3 /home/scripts/vpn_configuration/starter_vpn.py\nexit 0\nEOF")
	os.system()

if __name__ == '__main__':
	main()