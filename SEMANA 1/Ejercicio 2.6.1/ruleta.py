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

"""
Reglas:

"""