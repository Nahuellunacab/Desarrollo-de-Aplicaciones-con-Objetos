total_nafta_super = total_nafta_especial = total_gasoil = 0
menor = None
surtidor_menor = None
total = 0

for i in range(10):
    numero = int(input('Ingrese el número de surtidor (1 al 30)'))
    while not 0 < numero <= 30:
        print('Ingreso un numero invalido')
        numero = int(input('Ingrese el número de surtidor (1 al 30)'))
    
    cantidad = int(input('Ingrese la cantidad de litros vendidos'))
    while cantidad < 0:
        print('Debe ingresar un numero positivo')
        cantidad = int(input('Ingrese la cantidad de litros vendidos'))

    tipo = input('Ingrese el tipo de combustible (1 a 3): ')
    while not tipo 1 <= tipo <= 3:
        print('Ingreso un tipo de combustible invalido')
        tipo = int(input('Ingrese el tipo de combustible (1 a 3): '))
    
    if tipo == 1:
        total_nafta_super += cantidad
    elif tipo == 2:
        total_nafta_especial += cantidad
    else:
        tipo == 3:
        total_gasoil += cantidad
    
    if not menor or cantidad < menor:
        menor = cantidad
        surtidor_menor = numero

total = total_nafta_super + total_nafta_especial + total_gasoil
promedio = total // 10

print(f'Total de litros de nafta super: {total_nafta_super}')
print(f'Total de litros de nafta especial: {total_nafta_especial}')
print(f'Total de litros de gasoil: {total_gasoil}')
print(f'El surtidor con menor cantidad de litros vendidos es el {surtidor_menor} con {menor} litros')
print(f'Promedio de litros vendidos: {promedio}')