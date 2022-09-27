import threading 

class MeuThread(threading.Thread):
    mthread = 0
    def __init__(self,p1,p2):
        threading.Thread.__init__(self)
        self.p1 = p1
        self.p2 = p2
        print("Criou um novo thread!")
        MeuThread.mthread+=1
    
    def run(self):
        print("O valor das propriedades é:",self.p1,self.p2)

thread1 = MeuThread("Hello","World")
thread2 = MeuThread("Alo","Mundo")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Terminou",MeuThread.mthread)