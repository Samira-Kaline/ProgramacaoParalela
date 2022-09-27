import threading 

class MeuThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        print("Criou um novo thread!")
    
    def run(self):
        print("Executou o metodo run()!")

thread1 = MeuThread()
thread2 = MeuThread()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Terminou")