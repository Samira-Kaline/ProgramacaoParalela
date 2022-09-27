import threading 

class MeuThread(threading.Thread):

    def __init__(self,lista_desordenada):
        threading.Thread.__init__(self)
        self.lista_desordenada = lista_desordenada
        print("Criou um novo thread!")
    
    def run(self):   
        print("A lista ordenada:",self.lista_desordenada.sort())

thread1 = MeuThread([1,2,3,4,5,6,7,8,9,10])
thread2 = MeuThread([0,9,8,7,6,5,4,3,2,1])

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Terminou")