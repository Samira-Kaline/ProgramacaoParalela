import socket

HOST = "10.10.133.44" # Endereço ou hostname do servidor
PORT = 5432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
while True:
  entrada = input()
  if(entrada=='Sair'):
    break
  s.sendall(entrada.encode())
  data = s.recv(1024)
  print("Recebeu ", data.decode())