"""
# ----------------------
# Created : 26-11-2021 10:45
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""

import socket
import subprocess
import sys
from datetime import datetime


def read_host():
    """Function to read remote host IP"""

    subprocess.call("cls", shell=True)

    # Input scanning
    remote_server = input("Enter a remote host to scan: ")
    remote_ip = socket.gethostbyname(remote_server)

    # Print a nice banner with information on which host we are about to scan
    print("^" * 40)
    print("Please wait, scanning remote host", remote_ip)
    print("v" * 40)
    return remote_ip;


def port_scan(ip):
    """Function to scan remote host IP"""
    t1 = datetime.now()  # Check what time the scan started
    try:
        for port in range(1, 81):  # scanning port from 1 to 80
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                if port == 80:
                    print("Port HTTP ({}) is open".format(port))
                elif port == 22:
                    print("Port SSH ({}) is open".format(port))
                else:
                    print("No port")
            sock.close()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)


if __name__ == "__main__":
    ip = read_host()  # To read remote host
    port_scan(ip)  # To get open ports
