# Desafío Ascensor

## Enunciado
Se debía implementar una clase `Ascensor` que represente el funcionamiento de un ascensor, con las siguientes características:

- El ascensor tiene una **capacidad máxima de personas**.
- Puede operar entre un **piso mínimo** y un **piso máximo**.
- Inicialmente se encuentra en el piso **0**, que debe estar dentro del rango de pisos permitido.
- Atributos principales:
  - `piso_actual`
  - `personas`
  - `capacidad`
  - `piso_minimo`
  - `piso_maximo`

### Métodos solicitados
- `ir_a_piso(piso)`: mueve el ascensor al piso indicado si está en el rango válido. Retorna `True` o `False`.
- `subir(cantidad)`: suben personas al ascensor.
  - Si la cantidad es inválida (≤ 0) retorna `-1`.
  - Si entran todas, retorna esa cantidad.
  - Si entran solo algunas por límite de capacidad, retorna cuántas pudieron subir.
- `bajar(cantidad)`: bajan personas del ascensor.
  - Si la cantidad es inválida (≤ 0) retorna `-1`.
  - Si hay suficientes, bajan esa cantidad.
  - Si quieren bajar más de las que hay, bajan todas.
- `__str__`: devuelve un string con el estado actual (piso y personas).

El constructor debe lanzar un `ValueError` si:
- `piso_minimo > piso_maximo`
- `capacidad <= 0`
- el piso inicial `0` no está en el rango `[piso_minimo, piso_maximo]`.

---

## Implementación

Archivo: **ascensor.py**

```python
class Ascensor:
    def __init__(self, piso_minimo, piso_maximo, capacidad):
        if piso_minimo > piso_maximo:
            raise ValueError("El piso mínimo no puede ser mayor al piso máximo")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser positiva")
        if not (piso_minimo <= 0 <= piso_maximo):
            raise ValueError("El piso inicial 0 no está dentro del rango permitido")

        self.piso_minimo = piso_minimo
        self.piso_maximo = piso_maximo
        self.capacidad = capacidad
        self.piso_actual = 0
        self.personas = 0

    def ir_a_piso(self, piso_destino):
        if self.piso_minimo <= piso_destino <= self.piso_maximo:
            self.piso_actual = piso_destino
            return True
        return False

    def subir(self, cantidad):
        if cantidad <= 0:
            return -1
        espacio_disponible = self.capacidad - self.personas
        if cantidad <= espacio_disponible:
            self.personas += cantidad
            return cantidad
        else:
            self.personas = self.capacidad
            return espacio_disponible

    def bajar(self, cantidad):
        if cantidad <= 0:
            return -1
        if cantidad <= self.personas:
            self.personas -= cantidad
            return cantidad
        else:
            cantidad_bajada = self.personas
            self.personas = 0
            return cantidad_bajada

    def __str__(self):
        return f"Ascensor en piso {self.piso_actual} con {self.personas} personas"
```

---

## Tests automáticos

Archivo: **test_ascensor.py** (dado por la cátedra).

### Estructura
Se utiliza pytest. Cada función `test_...` valida un aspecto del ascensor:

- `test_ir_a_piso_valido`: Verifica que el ascensor se mueva a un piso dentro del rango.
- `test_ir_a_piso_invalido`: Intenta moverse a un piso fuera del rango. Debe retornar False y no cambiar `piso_actual`.
- `test_subir_personas`: Sube personas respetando la capacidad máxima.
- `test_subir_invalido`: Intenta subir 0 o números negativos. Debe retornar -1 y no cambiar el estado.
- `test_bajar_personas`: Baja personas de forma correcta y también el caso en que bajen más de las que hay (todas salen).
- `test_bajar_invalido`: Intenta bajar cantidades inválidas (≤ 0).
- `test_constructor_piso_inicial_cero_dentro_de_rango`: Comprueba que el ascensor arranca en 0. Si 0 no está en el rango, debe lanzar ValueError.
- `test_constructor_parametros_invalidos`: Si la capacidad es ≤ 0 o el rango de pisos es inválido, debe lanzar ValueError.

---

## Cómo ejecutar los tests

1. Instalar pytest:
   ```bash
   pip install pytest
   ```

2. Ubicarse en la carpeta del proyecto y ejecutar:
   ```bash
   python -m pytest -v
   ```

3. Si todo está correcto, la salida debe mostrar:

```
collected 8 items

test_ascensor.py::test_ir_a_piso_valido PASSED
test_ascensor.py::test_ir_a_piso_invalido PASSED
test_ascensor.py::test_subir_personas PASSED
test_ascensor.py::test_subir_invalido PASSED
test_ascensor.py::test_bajar_personas PASSED
test_ascensor.py::test_bajar_invalido PASSED
test_ascensor.py::test_constructor_piso_inicial_cero_dentro_de_rango PASSED
test_ascensor.py::test_constructor_parametros_invalidos PASSED

8 passed in 0.06s
```

---

## Conclusiones

Con este desafío se practica:

- Definición de clases con atributos de estado.
- Validaciones en el constructor.
- Control de invariantes (capacidad, rango de pisos).
- Manejo de casos inválidos en métodos.
- Uso de pytest para validar automáticamente el comportamiento.

Este ejercicio muestra cómo los tests automáticos ayudan a garantizar que el código cumple exactamente con el enunciado.
