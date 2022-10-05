import sys
import os

rpaifilho,wpaifilho = os.pipe()

rfilhopai,wfilhopai = os.pipe()

comando = ["/usr/bin/bc","-ls"]
processid = os.fork()
if processid==0:
  os.dup2(rpaifilho,sys.stdin.fileno())
  os.close(wpaifilho)
  os.dup2(wfilhopai,sys.stdout.fileno())
  os.close(rfilhopai)
  os.execve(comando[0],comando,os.environ)
else:
  os.close(rpaifilho)
  escrita = os.fdopen(wpaifilho,'w')
  os.close(wfilhopai)
  leitura = os.fdopen(rfilhopai,'r')
  print("Digite uma expressao(quit para sair)")
  linha = input()
  while(linha!=" "):
    if(linha=="\n"):
      linha = input()
      continue
    escrita.write(linha+"\n")
    escrita.flush()
    resposta = leitura.readline()
    if resposta !="":
      print("Resposta:",resposta)
    else:
      break
    print("Digite uma expressao(quit para sair)")
    linha = input()