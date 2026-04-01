# PORT SCANNER v3

import socket  # Used to establish a connection with the internet
from IPy import IP  # Module used for handling IPv4 and IPv6 addressess and networks


def scan(target):
    converted_ip = check_ip(target)  # This line calls the check_ip() function, passing the user input as an argument. The check_ip() function is responsible for validating the input and converting it to an IP address if necessary. If the input is already a valid IP address, it will simply return it. If the input is a hostname, it will attempt to resolve it to an IP address using the socket.gethostbyname() method.
    if converted_ip is None:  # If the domain could not be resolved, skip scanning
        return
    print("\n" + "Scanning Target: " + str(target))  # Print the target being scanned
    for port in range(20, 85):
        scan_port(converted_ip, port)  # This line calls the scan_port() function, passing the converted IP address and the current port number as arguments. This loop iterates through a range of ports from 20 to 84 to perform the scanning process on each of those ports for the given target.


def check_ip(ip):
    try:
        IP(ip)
        return ip  # If the input is already a valid IP address, return it as is
    except ValueError:
        try:
            return socket.gethostbyname(ip)  # If the user inputs a hostname instead of an IP address, this function will attempt to convert it to an IP address using the socket.gethostbyname() method.
        except socket.gaierror:
            print("[-] Cannot resolve: " + ip)  # If the domain cannot be resolved, print an error message
            return None


def get_banner(s):
    # 1024 is the buffer size, it means that the program will receive up to 1024 bytes of data from the socket. This is typically used to read the banner information from a service running on the open port, which can provide details about the service and its version.
    return s.recv(1024)


def scan_port(ipaddress, port):  # function that scans the ports
    try:
        sock = socket.socket()
        sock.settimeout(1.5)  # this written because the program takes a lot of time to get the ping so we have a timeout of 1.5sec and if there is no answer it moves to the next port
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            # This line is used to print the open port and its corresponding banner information. The banner is decoded from bytes to a string using the decode() method, and any leading or trailing newline characters are removed using the strip('\n') method.
            print("[+] Port {} is open: {}".format(port,
                  banner.decode().strip('\n')))
        except:
            print("[+] Port {} is open but no banner received".format(port))
        sock.close()  # Close the socket after use to free up resources
    except:
        pass  # If the port is closed or connection fails, move to the next port


if __name__ == "__main__":
    # Asking the user to input the desired IP address or domain to scan
    targets = input("[+] Enter Target/s To Scan (split multiple targets with ,): ")
    if "," in targets:
        for ip_add in targets.split(","):  # This line checks if the user has entered multiple targets by looking for a comma in the input. If a comma is found, it splits the input string into individual targets.
            scan(ip_add.strip(" "))  # The strip(" ") method removes any leading or trailing whitespace from each target before passing it to the scan() function.
    else:
        scan(targets)  # If only one target is entered, scan it directly
