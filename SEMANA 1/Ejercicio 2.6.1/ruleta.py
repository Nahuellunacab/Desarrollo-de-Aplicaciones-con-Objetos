""" 
Simulador de Ruleta

Desarrollar un programa que simimule el juego de la ruleta.

Para ello generar al azar 1000 tirada y luego informar:

* Cantidad de pares e impares
* Cantidad de tiradas por cada docena
* Porcentaje de ceros sobre el total de jugadas
* Cantidad de rojos y negros
"""

import random
from rich import print
from rich.console import Console   
from rich.panel import Panel
from rich.table import Table   
from typing import List, Tuple

"""
Reglas:

Comuenza en 1, R (1-ROJO)
Los números negros N son aquellos cuya reducción es PAR, o sea, la suma de sus digitos es divisible por 2
"""

console = Console()

def reducir_numero(numero:int) -> int:
    """La función toma un número entero y devuelve un entero que es igual a la suma de todos sus digitos.
    Si lasuma tiene dos digitos repite el proceso hasta que salga un solo digito.

    :param numero: Número que se desea reducir
    :type numero: int
    :return: valor de UN digito, obtenido a partir de la suma de los digitos del número original.
    :rtype: int
    """

    # Caso base: Si el número tiene un solo dígito, devolverlo tal cual
    if numero < 10:
        return numero
    # Convertir el número en una lista de digitos.
    digitos = [int(digito) for digito in str(numero)]
    # Calcular la suma de los digitos
    suma_digitos = sum(digitos)
    # Llamar recursivamene a la función con la suma de los digitos
    return reducir_numero(suma_digitos)

def get_color (nro: int) -> str:
    """ Dado un número de la ruleta, determinar el color de dicho número en el paño
    
    :param nro: Número del cual se desea averiguar el color
    :type nro: int
    :return: Color del número indicado. Valores validos: V (verde), R (rojo), N (negro)
    :rtype: str
    """

    if nro == 0:
        return 'V'
    elif nro == 10 or nro == 28:
        return 'N'
    else:
        # Los números negros son los pares
        # Aquellos cuya reducción es par
        # El 10 y el 28
        if reducir_numero(nro)%2 == 0:
            return 'N'
        else:
            return 'R'

def generar_ruleta():
    """Genera un tablero de ruleta, como una lista de tuplas conteniendo (número, color)
    """

    ruleta = []
    for nro in range (0,37):
        ruleta.append((nro, get_color(nro)))
    return ruleta

def imprimir_ruleta(rul: List[Tuple[int, str]]):
    """Imprime por consola un paño de ruleta, obtenido por medio de una lista de tuplas

    :param rul: lista que representa el paño de la ruleta
    :type rul: lista de tuplas (numero, color)
    """

    col = 1
    for nro, color in rul:
        if color == 'V':
            console.print(f"[bold white on green] {nro:^12}[/]", end="")
            print()
        elif color == 'R':
            console.print(f"[bold white on green] {nro:^4}[/]", end="")
        else:
            console.print(f"[bold white on black] {nro:^4}[/]", end="")
            col += 1
        if col == 4:
            print()
            col = 1

def imprimir_tirada(nro: int, color: str):
    if color == 'V':
        console.print(f"Obtuvimos [bold white on green] {nro}{color}[/]")
    elif color == 'R':
        console.print(f"Obtuvimos [bold white on red] {nro}{color}[/]")
    else:
        console.print(f"Obtuvimos [bold white on black] {nro}{color}[/]")   

def simulacion(ruleta: List[Tuple[int, str]]):
    cantidad_pares = cantidad_impares = 0
    cantidad_rojos = cantidad_negros = 0
    tiradas_primera_docena = tiradas_segunda_docena = tiradas_tercera_docena = 0
    cantidad_ceros = 0
    jugadas = 1000

    for i in range(jugadas):
        tirada_nro = random.randint(0,36)
        tirada_color = ruleta[tirada_nro][1]

        if tirada_nro % 2 == 0:
            cantidad_pares += 1
        else:
            cantidad_impares += 1

        if tirada_color == 'R':
            cantidad_rojos += 1
        elif tirada_color == 'N':
            cantidad_negros += 1
        else:
            cantidad_ceros += 1

        # Docenas
        if 1 <= tirada_nro <= 12:
            tiradas_primera_docena += 1
        elif 13 <= tirada_nro <= 24:
            tiradas_segunda_docena += 1
        elif 25 <= tirada_nro <= 36:
            tiradas_tercera_docena += 1
        # El 0 no suma en ninguna docena

    porcentaje_ceros = cantidad_ceros * 100 / jugadas

    console.print()
    table = Table(title="Resultados de la simulación")
    table.add_column("Resultado")
    table.add_column("valor", justify="center")
    table.add_row("Cantidad de pares", str(cantidad_pares))
    table.add_row("Cantidad de impares", str(cantidad_impares))
    table.add_row("Cantidad de tiradas 1a docena", str(tiradas_primera_docena))
    table.add_row("Cantidad de tiradas 2a docena", str(tiradas_segunda_docena))
    table.add_row("Cantidad de tiradas 3a docena", str(tiradas_tercera_docena))
    table.add_row("Porcentaje de ceros", str(porcentaje_ceros) + "%")
    table.add_row("Cantidad de rojos", "[bold white on red]" + str(cantidad_rojos))
    table.add_row("Cantidad de negros", "[bold white on black]" + str(cantidad_negros))
    console.print(table)

def principal():
    ruleta = generar_ruleta()
    imprimir_ruleta(ruleta)
    simulacion(ruleta)

if __name__ == "__main__":
    principal()