from multiprocessing.shared_memory import *
from array import *

memoria = SharedMemory(name="Minhamemoria",create=False,size=1024)

print("Informe o tamanho da lista:",end=" ")

tamanho = int(input())

lista = list(array('b',memoria.buf[:tamanho]))
print("lista de numeros: ",lista)
