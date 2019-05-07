def suma(x,y):
    z=x+y
    print(z)
    resta(x,y)
def resta(x,y):
    z=x-y
    print(z)
    multiplicacion(x,y)
def multiplicacion(x,y):
    z=x*y
    print(z)
    division(x,y)
def division(x,y):
    z=x/y
    print(z)
def ingreso():
    x=int(input("ingresar dato"))
    y=int(input("ingresar dato"))
    suma(x,y)
ingreso() 

