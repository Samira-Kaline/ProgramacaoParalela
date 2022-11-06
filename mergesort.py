from multiprocessing import shared_memory
import os

def merge(vetor, p, meio, u):
  L = []
  R = []
  for i in range(p, meio + 1):
    L.append(vetor[i])
  for i in range(meio + 1, u + 1):
    R.append(vetor[i])
  k = p
  while (len(L) > 0 and len(R) > 0):
    if (int(L[0]) < int(R[0])):
      vetor[k] = L.pop(0)
    else:
      vetor[k] = R.pop(0)
    k += 1
  while (len(L) > 0):
    vetor[k] = L.pop(0)
    k += 1
  while (len(R) > 0):
    vetor[k] = R.pop(0)
    k += 1


def mergeSort(vetor, p, u):
  if (p < u):
    meio = int((p + u) // 2)
    mergeSort(vetor, p, meio)
    mergeSort(vetor, meio + 1, u)
    merge(vetor, p, meio, u)


print("Informe um vetor de numeros", end=" ")
vetor = list(map(int, input().split()))
if(os.fork()==0):
  vetor = shared_memory.ShareableList(vetor)
  vetor.shm.unlink()
  mergeSort(vetor, 0, len(vetor) - 1)
  print(vetor)
  exit(0)
os.wait()
