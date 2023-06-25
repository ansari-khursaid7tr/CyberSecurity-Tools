"""
To run this script open the terminal and run the following command with superuser do:
python mac_changer.py -i [interface_name] -m [new_mac_address]
"""

import optparse
import subprocess

class MAC_Changer:
    def __init__(self, interface, new_mac):
        self.interface = interface
        self.new_mac = new_mac

    def change_mac(self):
        print("[+] Changing MAC for interface " + self.interface + " to " + self.new_mac)
        subprocess.call(["ifconfig", self.interface, "down"])                         # Disable the specified interface
        subprocess.call(["ifconfig", self.interface, "hw", "ether", self.new_mac])    # Set the new MAC address for the specified interface
        subprocess.call(["ifconfig", self.interface, "up"])                           # Enable the specified interface

def get_arguments():
    """
    Get the command line arguments provided by the user.
    """
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Specify interface to change the MAC for, use --help for usage")
    parser.add_option("-m", "--mac", dest="new_mac", help="Specify the new MAC, use --help for usage")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify interface as: \n python mac_changer.py -i [interface_name] -m [new_mac_address]")
    elif not options.new_mac:
        parser.error("[-] Please provide a valid mac address, use --help for usage")
    return options

def main():
    options = get_arguments()                                          # Get the user provided arguments
    mac_changer = MAC_Changer(options.interface, options.new_mac)      # Change the MAC address of the specified interface to the new MAC address
    mac_changer.change_mac()

if __name__ == "__main__":
    main()