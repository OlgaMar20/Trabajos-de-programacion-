def mensaje(msg):
    print(x)

x = "Hola Mundo"

mensaje(x)
x="Hola mundo"
x:int=10

print(x)

print(x)

# %%
print ("Hola ICI")
x=10

# %%
print ("Hola")
print (x)

# %%
x=10
print(x,":",id(x))

x=x+1
print(x,":",id(x))

# %%
def mensaje(msg:str):
    print("Dentro de la funcion",msg,id(msg))

x = "Hola Mundo"
print("Fuera de la funcion",x,id(x))
mensaje(x)
# %%
if __name__=="__main__":
    mensaje("Hola Mundo")

def saludo_edad_(nombre:str,a_nacimiento:int):
    edad= 2022-a_nacimiento
    print("Hola",nombre,"tienes",edad,"años")
if __name__=="__main__":
    saludo_edad_("Olga",2003)