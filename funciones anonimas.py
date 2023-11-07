# Programacion Funcional:
##  -Habrá ocaciones en las cuales necesitemos crear funciones de manera rápida, en tiempo de ejecución.
##  -Funciones las cuales realizan una tarea en concreto, regularmente pequeña.
##     En estos casos haremos uso de funciones lamda.
##  -Una funcion lamda es una funcion anonima, una fncion que no posee nombre. En python 
##     la estructura de una funcion lamda es la siguiente. 

# variable donde se guarda la lamda # = lambda (params) : lo que retorna
suma = lambda val1=0,val2=0: val1 + val2

print(suma) # output: <function <lambda> at 0x7f72bda47d90>

operacion = lambda operacion, val1=0,val2=0: operacion(val1, val2)
resultado = operacion(suma, 20, 10)

print( resultado ) # output: 30
resultado = operacion(suma)
print( resultado ) # output: 0


## ¿Que paso aqui?
## almacenamos una funcion lamda que suma dos numeros, en una variable suma, no creamos una funcion, solo una lamda
## almacenamos una funcion lamda que llama una funcion lamda que se pasa por parametro, y a la funcion lamda se le agregan dos parametros mas
## almacenamos lo que devuelve la funcion lamda (suma ) que se vuelve a devolver (operacion) en una variable resultado  



