from multiprocessing.shared_memory import *
memoria = SharedMemory(name="Minhamemoria",create = True,size=1024)

print("Informe uma lista de mumeros",end=" ")

lista = list(map(int,input().split()))

memoria.buf[:len(lista)] = bytearray(lista)

input("Agora você deve excutar o outro programa e informar o tamanho da lista ({:})".format(len(lista)))

memoria.close()

memoria.unlink()