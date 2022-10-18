from multiprocessing import shared_memory
import os

def merge(vetor,aux,e,meio,d):
  for k in range(e,d+1):
    aux[k] = vetor[k]
  i = e
  j = meio+1
  for k in range(e, d + 1):
    if i > meio:
      vetor[k] = aux[j]
      j += 1
    elif j > d:
      vetor[k] = aux[i]
      i += 1
    elif aux[j] < aux[i]:
      vetor[k] = aux[j]
      j += 1
    else:
      vetor[k] = aux[i]
      i += 1

def mergeSort(vetor, aux, e, d):
  if d<= e:
      return
  meio = (e + d // 2)

  mergeSort(vetor, aux, e, meio)

  mergeSort(vetor, aux, meio + 1, d)
    

  merge(vetor, aux, e, meio, d)


print("Informe um vetor de numeros",end=" ")
vetor = list(map(int,input().split()))
vetor = shared_memory.ShareableList(vetor)
print("Arranjo não ordenado: ", vetor)
aux = [0] * len(vetor)
mergeSort(vetor, aux, 0, len(vetor) - 1)
os.wait
print("Arranjo ordenado:", vetor)
vetor.shm.unlink()