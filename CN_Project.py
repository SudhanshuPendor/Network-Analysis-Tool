import socket
import os
import platform

# 1. Get IP of a domain
def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP address of {domain}: {ip}")
    except socket.error as e:
        print(f"Error fetching IP: {e}")

# 2. Print IPv4 route table
def print_route_table():
    print("\nIPv4 Route Table:")
    if os.name == "nt":  # Windows
        os.system("route print -4")
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # Linux/MacOS
        os.system("netstat -nr | grep -v '::'")

# 3. Netstat command
def print_netstat():
    print("\nNetstat:")
    if os.name == "nt":  # Windows
        os.system("netstat -an")
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # Linux/MacOS
        os.system("netstat -an | grep -v '::'")

# 4. Traceroute (Hops)
def traceroute(domain):
    print(f"\nTraceroute for {domain}:")
    if os.name == "nt":  # Windows uses 'tracert'
        os.system(f"tracert {domain}")
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # Linux/MacOS
        os.system(f"traceroute {domain}")

# 5. Ping Path (Simple version of ping)
def ping(domain):
    print(f"\nPinging {domain}:")
    if os.name == "nt":  # Windows
        os.system(f"ping {domain}")
    elif platform.system() == "Linux" or platform.system() == "Darwin":  # Linux/MacOS
        os.system(f"ping -c 4 {domain}")

# Main Function
if __name__ == "__main__":
    domain = input("Enter the domain name: ")
    
    # Execute each of the network functions
    get_ip(domain)
    ping(domain)
    print_route_table()
    print_netstat()
    traceroute(domain)
    
