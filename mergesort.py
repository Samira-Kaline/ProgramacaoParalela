from multiprocessing import shared_memory
import os

def merge(vetor,p,meio,u):
  L = vetor[p:meio+1]
  R = vetor[meio+1:u+1]
  k = p
  while(len(L)>0 and len(R)>0):
    if(int(L[0])<int(R[0])):
      vetor[k] = L.pop(0)
    else:
      vetor[k] = R.pop(0)
    k+=1
  while(len(L)>0):
    vetor[k] = L.pop(0)
    k+=1
  while(len(R)>0):
    vetor[k] = R.pop(0)
    k+=1
  
def mergeSort(vetor,p,u):
  if(p<u):
    meio = int((p+u)/2)
    if(os.fork()==0):
      mergeSort(vetor,p,meio)
      exit(0)
    if(os.fork()!=0):
      mergeSort(vetor,meio+1,u)
      exit(0)
    merge(vetor,p,meio,u)

print("Informe um vetor de numeros",end=" ")
vetor = list(map(int,input().split()))
vetor = shared_memory.ShareableList(vetor)
mergeSort(vetor,0,len(vetor)-1)
os.wait()
print(vetor)
vetor.shm.unlink()