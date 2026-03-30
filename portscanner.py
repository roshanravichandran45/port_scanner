# a very simple PORT SCANNER 
#my website ip 172.20.10.1 for test purposes 

import socket # Used to establish a connection with the internet 
from IPy import IP # Module used for handling IPv4 and IPv6 addressess and networks 

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port): #function that scans the ports 
    try:
        sock = socket.socket()
        sock.settimeout(1.0)   #this written because the program takes a lot of time to get the ping so we have a timeout of 0.5sec and if there is no answer it moves to the next port
        sock.connect((ipaddress, port))
        print("[+] Port " + str(port) + " is open")
    except: 
        print("[-] Port " + str(port) + " is closed")

ipaddress = input("[+] Enter Target To Scan: ") # Asking the user to input the desired IP address to scan 
converted_ip = checkip(ipaddress)

for port in range(20,85):
    scan_port(converted_ip, port)