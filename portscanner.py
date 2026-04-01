<<<<<<< HEAD
# a very simple PORT SCANNER

import socket  # Used to establish a connection with the internet
from IPy import IP  # Module used for handling IPv4 and IPv6 addressess and networks


def scan(target):
    converted_ip = check_ip(target)  # This line calls the check_ip() function, passing the user input (targets) as an argument. The check_ip() function is responsible for validating the input and converting it to an IP address if necessary. If the input is already a valid IP address, it will simply return it. If the input is a hostname, it will attempt to resolve it to an IP address using the socket.gethostbyname() method. The resulting IP address is then stored in the variable converted_ip for further use in the scanning process.
    # This line is used to print the target that is being scanned. It concatenates the string "Scanning Target: " with the string representation of the targets variable, which contains the user input for the target IP address or hostname. The resulting message is printed to the console to indicate which target is currently being scanned.
    if converted_ip is None:  # If the check_ip() function returns None, it means that the input was invalid and could not be resolved to an IP address. In this case, the program will print an error message indicating that the target is invalid and will then return from the scan() function, effectively skipping the scanning process for that target.
        return
    print("\n" + " :) Scanning Target: " + str(target))
    for port in range(20, 85):
        scan_port(converted_ip, port)  # This line calls the scan_port() function, passing the converted IP address (converted_ip) and the current port number (port) as arguments. The scan_port() function is responsible for attempting to establish a connection to the specified IP address and port, and if successful, it will check for any banner information from the service running on that port. This loop iterates through a range of ports from 20 to 84 (inclusive) to perform the scanning process on each of those ports for the given target.
=======
# a very simple PORT SCANNER 
>>>>>>> 7177fa47c22f3f977690621cfb74fc7988dcc899


def check_ip(ip):
    try:
        IP(ip)
        return (ip)
    except ValueError:
        # This line is used to resolve the hostname to an IP address. If the user inputs a hostname instead of an IP address, this function will attempt to convert it to an IP address using the socket.gethostbyname() method. If the input is already a valid IP address, it will simply return it.
        try:
            return socket.gethostbyname(ip)
        except:
            # If the hostname cannot be resolved to an IP address, it will print an error message indicating that the resolution failed and will then return None to indicate that the input was invalid. This allows the program to handle cases where the user inputs an invalid hostname or IP address gracefully without crashing.
            print("[-] Cannot resolve: " + ip)
            return None


def get_banner(s):
    # 1024 is the buffer size, it means that the program will receive up to 1024 bytes of data from the socket. This is typically used to read the banner information from a service running on the open port, which can provide details about the service and its version.
    return s.recv(1024)


def scan_port(ipaddress, port):  # function that scans the ports
    try:
        sock = socket.socket()
        # this written because the program takes a lot of time to get the ping so we have a timeout of 0.5sec and if there is no answer it moves to the next port
        sock.settimeout(1.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            # This line is used to print the open port and its corresponding banner information. The banner is decoded from bytes to a string using the decode() method, and any leading or trailing newline characters are removed using the strip('\n') method. The resulting string is then formatted into the output message that indicates which port is open and what banner information was received from the service running on that port.
            print("[+] Port {} is open: {}".format(port,
                  banner.decode().strip('\n')))
        except:
            print("[+] Port {} is open but no banner received".format(port))
    except:
        pass


<<<<<<< HEAD
# Asking the user to input the desired IP address to scan
if __name__ == "__main__":
    targets = input(
        "[+] Enter Target To Scan, split multiple targets with a comma: ")
    if "," in targets:
        for ip_add in targets.split(","):  # This line checks if the user has entered multiple targets by looking for a comma in the input. If a comma is found, it splits the input string into individual IP addresses using the split(",") method and iterates through each IP address in the resulting list. For each IP address, it calls the scan() function to perform the port scanning.
            # The strip(" ") method is used to remove any leading or trailing whitespace from the IP address before passing it to the scan() function. This ensures that the IP addresses are properly formatted and do not contain any extra spaces that could cause issues during the scanning process.
            scan(ip_add.strip(" "))
    else:
        scan(targets)
=======
for port in range(20,85):
    scan_port(converted_ip, port)
>>>>>>> 7177fa47c22f3f977690621cfb74fc7988dcc899
