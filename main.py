
# %%
def saludo_edad_(nombre:str,a_nacimiento:int):
    edad= 2022-a_nacimiento
    print("Hola",nombre,"tienes",edad,"años")

def calcular_edad(a_actual:int,a_nacimiento:int)->int:
    return a_actual-a_nacimiento

def saludo(nombre:str,edad:int):
    print ("Hola",nombre,"tienes",edad,"años")

def cuadrados(numu:int,numd:int):
    return (numu*numu) + (numd*numd)
if __name__=="__main__":
    print(cuadrados(2,2))
# %%
def tabla(x):
    for i in range (11):
        print(x,"*",i,"=",x*i)


if __name__=="__main__":
    print(tabla(3))
# %%
#Clase del 12 de septiembre 
def tabla(t,n):
    for i in range (1,n+1):
        print(t,"*",i,"=",t*i)
if __name__=="__main__":
    print(tabla(3,2))
# %%
def tabla(t:int,n:int,spc:int):
    for i in range (1,t+1):
        for j in range (1,n+1):
            print(f""i,"*",j,"=",i*j)
t=int(input("¿Hasta que tablas quieres calcular?"))
n=int(input("¿Hasta que numero quieres calcular?"))
tabla(t,n)
# %%
def tabla(t:int,n:int,spc:int):
    for i in range (1,t+1):
        for j in range (1,n+1):
            print(f"{i:^{spc}} * {j:^{spc}} = {i*j:^{spc}}")
t=int(input("¿Hasta que tablas quieres calcular?"))
n=int(input("¿Hasta que numero quieres calcular?"))
spc=int(input("¿Que espaciado quieres?"))
tabla(t,n,spc)