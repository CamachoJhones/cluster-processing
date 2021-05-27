import os 
import sys

def returnLargest(lst):
    largest=0
    for x in range (0,len(lst)):
        if(int(lst[x])>largest):
            largest=lst[x]
    return largest

lst= os.listdir(sys.argv[1])
print(lst)
numeros=[]
i=0
for file in lst:
    numero= int(file[5:-4])
    numeros.append(numero)
    i+=1
grande=returnLargest(numeros)-1
ordenado=[]
for i in range( 0, grande):
    ordenado.append("frame"+str(i) +".png")

print(ordenado)
