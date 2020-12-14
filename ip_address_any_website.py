import socket as s

host = input("Write any website here to get its IP: ")
print(f'IP of {host} is {s.gethostbyname(host)}')