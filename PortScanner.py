#! /usr/bin/env python
from socket import *
import sys, time
from datetime import datetime

host = ''
max_port = 5000
min_port = 0

def scan_host(host, port, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)

		code = s.connect_ex((host, port))

		if code == 0:
			r_code = code
		s.close()
	except Exception, e:
		pass

	return r_code

def scan_ports():
	for port in range(min_port, max_port):
		try:
			response = scan_host(host, port)

			if not response:
				print("[*] Porta %d: Aberta" % (port))
		except Exception, e:
			pass
		except KeyboardInterrupt:
			print("\n[*] Saindo da Aplicacao...")
			sys.exit(1)
def get_host()		
	try:
		host = raw_input("[*] Endereco Alvo: ")
	except KeyboardInterrupt:
		print("\n[*] Saindo da Aplicacao...")
		sys.exit(1)

	hostip = gethostbyname(host)

get_host()
print("\n[*] Host: %s IP: %s" % (host, hostip))
print("[*] Analizando, Inicio: %s \n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

scan_ports()

stop_time = datetime.now()
total_duration = stop_time-start_time
print("\n[*] Finalizado as %s" % (time.strftime("%H:%M:%S")))
print("[*] Duracao: %s" % (total_duration))
