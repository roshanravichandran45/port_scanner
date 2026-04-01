# Port Scanner

A Python-based port scanner that scans a range of ports on a target IP or domain name.

## Version History
- **v3.0** - Banner grabbing, multiple target scanning, invalid domain handling
- **v2.0** - Port range scanning, domain name support, timeout
- **v1.0** - Basic single port (80) scanner

## Requirements

- Python 3.x
- IPy library → install with: pip install IPy

## How to Use

1. Clone or download this repository
2. Run the script: python portscanner.py
3. Enter a target IP or domain name when prompted
4. To scan multiple targets, separate them with a comma

## Example
```
[+] Enter Target/s To Scan (split multiple targets with ,): scanme.nmap.org, google.com
[+] Port 22 is open: SSH-2.0-OpenSSH_6.6.1p1
[+] Port 80 is open but no banner received
[-] Cannot resolve: <User Input>
```

## Features

### v3.0
- Grabs banner information from open ports to identify running services
- Scans multiple targets in a single run by separating with a comma
- Handles invalid or unresolvable domains gracefully with a clear error message

### v2.0
- Scans a range of ports (20-85)
- Accepts domain names as input and converts them to IP addresses
- 1 second timeout per port for faster scanning

### v1.0
- Scans port 80 only on a target IP address

## Tradeoffs
- A 1.5 second timeout per port keeps scans reasonably fast but may miss 
ports that are slow to respond

## Planned Upgrades (v4)
- Let the user define the port range
- Show service names next to open ports (e.g. port 22 = SSH)
- Threading for faster scans across large port ranges

## Author
Roshan Ravichandran