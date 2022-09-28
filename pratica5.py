import threading
import sys

def procedimento(p1):
  print(p1)

listadeThreads = []

if(len(sys.argv)!=2):
  print("Você deve usar ",sys.argv[0],"<numero de Threads>")
  exit(1)

for i in range(0,int(sys.argv[1])):
  aux = threading.Thread(target=procedimento,kwargs={'p1':i})
  listadeThreads.append(aux)

for i in listadeThreads:
  i.start()
  
for i in listadeThreads:
  i.join()