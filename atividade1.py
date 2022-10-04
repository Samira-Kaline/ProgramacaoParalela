import sys

def isNumber(i):
  if(i=='1' or '2' or '3' or '4' or '5' or '6'or '7' or '8' or '9' or '0'):
    return True
  return False

def Intervalo(posi):
  if(posi>=20 and posi<30):
    return 0
  elif(posi>=30 and posi<40):
    return 1
  elif(posi>=40 and posi<60):
    return 2
  elif(posi>=60 and posi<70):
    return 3
  elif(posi>=70 and posi<100):
    return 4
  else:
    return 5

if(len(sys.argv)!=2):
  print("Voce deve usar: ",sys.argv[0],"<arquivo de entrada>")
  exit(1)

with open (sys.argv[1],"r") as arquivo:
  entrada = arquivo.readlines()
aux = [0,0,0,0,0,0]
for linha in entrada:
  lista = linha.split(" ")
  if(len(lista)>2):
    posi = Intervalo(int(lista[1]))
    aux[posi]+=1

print("20:",aux[0])
print("30:",aux[1])
print("40:",aux[2])
print("60:",aux[3])
print("70:",aux[4])
print("100:",aux[5])