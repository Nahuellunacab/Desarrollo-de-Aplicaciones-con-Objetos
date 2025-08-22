from validacion import *
from procesolistas import *

def cargar_temperaturas():

    temperaturas = []

    print('Ingrese las temperaturas entre -20 y 49. Finaliza con 50')
    t = ingresar_numero_entre('Ingrese una temperatura: ', -20, 50)
    while t != 50:
        temperaturas.append(t)
        t = ingresar_numero_entre('Ingrese una temperatura: ', -20, 50)

    return temperaturas 

def promedio_mayores(temperaturas, piso):

    cantidad = 0
    suma = 0

    for x in temperaturas:
        if x >= piso:
            suma += x
            cantidad += 1
        
    if cantidad == 0:
        promedio = 0
    else:
        promedio = suma / cantidad
        # promedio = suma /cantidad if cantidad != 0 else 0
    
    return promedio

def existe_mayor(temperaturas, piso):

    for x in temperaturas:
        if x > piso:
            return True
    return False

def mayor_dias_calidos(temperaturas):

    mayor = None
    for x in temperaturas:
        if x <= 20:
            if mayor is None or x > mayor:
                mayor = x
    return mayor 

def calcular(temperaturas):

    dias_bajo_cero = cantidad_menor(temperaturas, 0)
    promedio_todos = promedio(temperaturas)
    promedio_dias_calidos = promedio_mayores(temperaturas, 20)
    hubo_40_grados = existe(temperaturas, 40)
    mayor = mayor_dias_calidos(temperaturas)
    dias_menor_al_promedio = cantidad_menor(temperaturas, promedio_todos)

    print(f'Días bajo cero: {dias_bajo_cero}')
    print(f'Promedio de todas las temperaturas: {promedio_todos:.2f}')
    if (promedio_dias_calidos != 0):
        print(f'Promedio de días cálidos: {promedio_dias_calidos:.2f}')
    print('¿Hubo dias con mas de 40 grados?', "si" if hubo_40_grados else "no")
    if mayor:
        print(f'La mayor temperatura de los dias que no fueron cálidos: {mayor}')
    else:
        print('Todos los días fueron cálidos')
    
    print ("Hubo {dias_menor_al_promedio} días con temperaturas menores al promedio de todas las temperaturas")

    def principal():
        temperaturas = cargar_temperaturas()
        calcular(temperaturas)
    
    if __name__ == '__main__':
        principal()