# a very simple PORT SCANNER 

import socket # Used to establish a connection with the internet 
from IPy import IP # Module used for handling IPv4 and IPv6 addressess and networks 

# Declaring what are the inputs are as we need IP Address and the Port Number 

ipaddress = input("[+] Enter Target IP To Scan: ") # Asking the user to input the desired IP address to scan 
port = 80  # Just scanning the port 80

# Trying to establish the connection and checking if port 80 is open or not 

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print("[+] Port 80 is open")
except: 
    print("[-] Port 80 is closed")

