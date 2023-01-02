import os
import sys
from datetime import date


def main():


	print("Setting the reboot service")
	os.system("cp reboot_system.service /etc/systemd/system")
	os.system("systemctl enable reboot_system.service")
	os.system("systemctl start reboot_system.service")

	print("done")
if __name__ == '__main__':
	main()
