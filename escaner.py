import nmap

scanner = nmap.PortScanner()

ip = input("inserte dirrecion ip")
print("esta es la ip", ip)
scanner.scan(ip)

print(scanner.all_hosts())
