
import re
from threading import currentThread


mi_lista=[1,2,3,4]
print(mi_lista)
lista_vacia=[]
print(lista_vacia)
 

mi_lista2=[1,"Hola",True,3.14,[1,2,3],(1,2,3),{1,2,3}]
print(mi_lista2)

print(len(mi_lista))
print(len(mi_lista2))
print(f"Mi lista:{mi_lista}")

print(f"No de elementos:{len (mi_lista)}")
print(f"Primer elemento:{mi_lista[0]},{mi_lista[1]},{mi_lista[2]},{mi_lista[3]}")
print(f"Primer elemento:{mi_lista[-1]},{mi_lista[-2]},{mi_lista[-3]},{mi_lista[-4]}")

#Slices: rebanadas (partes de una lista)
print(mi_lista[1:-1])
print(mi_lista[0:3])
print(mi_lista[0:])
print(mi_lista[:])

#modificar elementos de la lista

mi_lista[2]="tres"
print(mi_lista)

#Insertar la lista [5,"seis",7,8] al final de la lista mi_lista 
new_lista=[5,"seis",7,8]
mi_lista[len(mi_lista):]=new_lista
print(mi_lista)

mi_lista=[1,2,3,4]
mi_lista.append("cinco")
print(mi_lista)

ml=[]
for i in range(1,5):
    ml.append(i)
print(ml)

#ml.append([6,7,8])
#print(ml)
ml.extend([6,7,8])
print(ml)

ml.insert(4,"cinco")
print(ml)

del ml[5]
print(ml)

ml.remove(2)
print(ml)

ml.reverse()
print(ml)

l1=[1,2,3]
l2=l1[:]
print(l1)
l1.reverse()
print(l1)
print(l2)

#Clase del 06 de septiembre 
ld=[[5,4,6],[7,8,2,1],[3,4,5],[6,7]]
print(f"Desordenado: {ld}")
ld.sort()
print(f"Ordenado: {ld}")

ld=[5,4,6,7,8,2,1,3,4,5,6,7]
S1= sorted(ld)
print(S1)
ld=[5,4,6,7,8,2,1,3,4,5,6,7]
S2= sorted(ld,reverse=True)
print(S2)

ceros=[0,0,0,0,0,0,0,0,0]
print(ceros)
ceros=[0]*9
print(ceros)

valor_max=max(ld)
print(valor_max)

valor_min=min(ld)
print(valor_min)

cuatros=ld.count(4)
print(cuatros)

repe=[]
for i in range (1,9):
    repe.append(ld.count(i))
print(repe)

#Escribe una funcion que reciba como argumentos T y N donde T
#  es el limite de tablas de multiplicar  que se desean obtener
# y N hasta un valor de las tablas se desea. Todas empiezan desde 1

def tablas(t:int,n:int):
    for i in range(1,t+1):
        tabla(i,n,10)

def tabla(t:int,n:int,spc:int):
    for i in range (1,n+1):
        print(f"{t:^{spc}}x{i:^{spc}}={t*i:^{spc}}")

t=int(input("¿Hasta que tablas quieres calcular?"))
n= int(input("¿Hasta que numero quieres calcular?"))
tablas(t,n)