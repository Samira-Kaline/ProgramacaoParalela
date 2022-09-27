from concurrent.futures import thread
import sys
import threading
import os
import cv2

class MeuThread(threading.Thread):
  def __init__(self,maxThread,pastaraiz,pastas,escala,destino):
    threading.Thread.__init__(self)
    self.maxThread = maxThread
    self.pastaraiz = pastaraiz
    self.pastas = pastas
    self.escala = escala
    self.destino = destino
    print("Criou um novo thread!")
    
  def run(self):
      print("Executou o metodo run()!")

if(len(sys.argv)!=5):
  print("voce deve usar",sys.argv[0],"<origem><escala><threads><destino>")
  exit(1)

pastaraiz = sys.argv[1]
escala = int(sys.argv[2])
maxThread = int(sys.argv[3])
destino = sys.argv[4]

Threads = []
print("Número máximos de Threads em paralelo ", maxThread)

sys.stdout.flush(pastaraiz)
pastas = os.listdir(pastaraiz)

for numero in range(0,maxThread):
  Thread = MeuThread(maxThread,pastaraiz,pastas,escala,destino)
  Threads.append(Thread)
  Thread.start()

for Thread in Threads:
  Thread.join()

print("concluido")
