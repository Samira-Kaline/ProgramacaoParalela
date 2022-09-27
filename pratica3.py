import sys
import threading 

class MeuThread(threading.Thread):
    mthread = 0
    def __init__(self):
        threading.Thread.__init__(self)
        print("Criou um novo thread!")
        MeuThread.mthread+=1
    
    def run(self):
        print("Executou o metodo run()!")

mlista = []
cont = int(sys.argv[1])

for i in range(cont):
    mlista.append(MeuThread())

for j in mlista:
    j.start()
    j.join()

print("Terminou",MeuThread.mthread)