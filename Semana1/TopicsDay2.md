# Continuación estudio de Python

## 🔵 Fundamentos

### ¿Qué es una lista y para qué sirve?

En Python, una lista es una estructura de datos que te permite almacenar múltiples elementos en un solo objeto. Es una colección ordenada y mutable, lo que significa que puedes modificar sus elementos, agregar nuevos o eliminarlos después de haberla creado.

Características de una lista:

    Ordenada: Los elementos de la lista tienen un orden específico. Cada elemento se puede acceder por su índice (su posición en la lista).

    Mutable: Puedes cambiar el contenido de la lista después de haberla creado (añadir, eliminar o modificar elementos).

    Heterogénea: Puedes almacenar diferentes tipos de datos en una misma lista, como números, cadenas de texto, e incluso otras listas.

Usos comunes de las listas:

    Almacenar secuencias de elementos: Como una lista de nombres, números, etc.

    Realizar operaciones sobre colecciones de datos: Como ordenar, filtrar, o buscar elementos en una lista.

    Trabajo con índices: Permiten acceder fácilmente a cualquier elemento usando su índice, por ejemplo mi_lista[0] para obtener el primer elemento.

    Iteración: Puedes recorrer las listas usando bucles, lo que facilita la manipulación de grandes cantidades de datos.

## ¿Porqué la creación de listas en python es con corchetes?

La elección de corchetes ([]) para crear listas en Python tiene que ver con el diseño del lenguaje y la forma en que se quiere distinguir entre diferentes tipos de estructuras de datos. 

## ¿Cómo accedo a los elementos de una lista?

### 1. Acceder por índice

Cada elemento de una lista tiene un índice que lo identifica de manera única. El índice empieza en 0, es decir, el primer elemento tiene el índice 0, el segundo tiene el índice 1, y así sucesivamente.

Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza']

#### Accediendo al primer elemento (índice 0)
    print(mi_lista[0])  # Imprime 'manzana'

#### Accediendo al segundo elemento (índice 1)
    print(mi_lista[1])  # Imprime 'banana'

#### Accediendo al último elemento (índice 2)
    print(mi_lista[2])  # Imprime 'cereza'

### 2. Acceder con índices negativos

Los índices negativos te permiten acceder a los elementos de la lista desde el final. Por ejemplo, -1 se refiere al último elemento, -2 al penúltimo, y así sucesivamente.

Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza']

#### Accediendo al último elemento con índice negativo
    print(mi_lista[-1])  # Imprime 'cereza'

#### Accediendo al penúltimo elemento
    print(mi_lista[-2])  # Imprime 'banana'

### 3. Acceder a un rango de elementos (slicing)

Puedes acceder a un subconjunto de elementos de la lista utilizando slicing (rebanado). La sintaxis es mi_lista[inicio:fin], donde:

    inicio es el índice de donde empieza el corte (inclusive).

    fin es el índice donde termina el corte (exclusivo).

Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza', 'naranja', 'pera']

#### Accediendo a los primeros tres elementos (índices 0, 1, 2)
    print(mi_lista[:3])  # Imprime ['manzana', 'banana', 'cereza']

#### Accediendo a los elementos desde el índice 2 hasta el final
    print(mi_lista[2:])  # Imprime ['cereza', 'naranja', 'pera']

#### Accediendo a un subconjunto entre los índices 1 y 3 (sin incluir el 3)
    print(mi_lista[1:3])  # Imprime ['banana', 'cereza']

### 4. Acceder a los elementos con un paso (slicing con paso)

Puedes especificar un paso adicional en el slicing. La sintaxis sería mi_lista[inicio:fin:paso], donde paso es la cantidad de elementos que se saltan entre cada uno de los seleccionados.

Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza', 'naranja', 'pera']

#### Accediendo a los elementos con paso 2
    print(mi_lista[::2])  # Imprime ['manzana', 'cereza', 'pera']

### 5. Iterar sobre la lista

Una forma común de acceder a los elementos de una lista es mediante un bucle for, lo que te permite recorrer todos los elementos de la lista.

Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza']

#### Usando un bucle para acceder a todos los elementos
    for fruta in mi_lista:
    print(fruta)

Esto imprimirá:

    manzana
    banana
    cereza

### 6. Acceder con el método enumerate()

Si también necesitas el índice de cada elemento mientras iteras sobre la lista, puedes usar el método enumerate().

Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza']

#### Usando enumerate() para obtener el índice y el valor
    for indice, fruta in enumerate(mi_lista):
    print(f"Índice {indice}: {fruta}")

Esto imprimirá:

    Índice 0: manzana
    Índice 1: banana
    Índice 2: cereza

## Resumen de métodos para acceder a los elementos:

    Índice positivo: mi_lista[0], mi_lista[1], etc.

    Índice negativo: mi_lista[-1], mi_lista[-2], etc.

    Slicing: mi_lista[inicio:fin]

    Iteración con for: Recorrer todos los elementos de la lista.

    enumerate(): Obtener el índice y el valor al iterar.

## ¿Cómo modifico los elementos de una lista?

En Python, las listas son mutables, lo que significa que puedes modificar sus elementos después de haberlas creado.

### 1. Modificar un elemento por su índice

Para cambiar el valor de un elemento en una lista, puedes acceder al elemento utilizando su índice y luego asignar un nuevo valor a esa posición.
Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza']

#### Cambiar el primer elemento (índice 0)
    mi_lista[0] = 'fresa'

    print(mi_lista)  # Imprime ['fresa', 'banana', 'cereza']

### 2. Modificar varios elementos con slicing

Puedes usar slicing para modificar múltiples elementos de una lista al mismo tiempo. Esto se hace asignando una nueva lista al slice de la lista original.
Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza', 'naranja']

#### Cambiar los dos primeros elementos
    mi_lista[0:2] = ['pera', 'kiwi']

    print(mi_lista)  # Imprime ['pera', 'kiwi', 'cereza', 'naranja']

### 3. Agregar elementos a la lista

Puedes agregar elementos de varias formas:

    Usando .append(): Agrega un solo elemento al final de la lista.

    Usando .extend(): Agrega varios elementos (una lista) al final de la lista.

    Usando .insert(): Agrega un elemento en una posición específica.

Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza']

#### Agregar un elemento al final
    mi_lista.append('naranja')
    print(mi_lista)  # Imprime ['manzana', 'banana', 'cereza', 'naranja']

#### Agregar varios elementos al final
    mi_lista.extend(['pera', 'kiwi'])
    print(mi_lista)  # Imprime ['manzana', 'banana', 'cereza', 'naranja', 'pera', 'kiwi']

#### Insertar un elemento en una posición específica
    mi_lista.insert(2, 'frambuesa')  # Insertar 'frambuesa' en el índice 2
    print(mi_lista)  # Imprime ['manzana', 'banana', 'frambuesa', 'cereza', 'naranja', 'pera', 'kiwi']

### 4. Eliminar elementos de la lista

Puedes eliminar elementos de la lista de diferentes maneras:

    Usando del: Elimina un elemento por su índice.

    Usando .remove(): Elimina el primer elemento que coincida con un valor específico.

    Usando .pop(): Elimina un elemento en una posición específica y lo devuelve.

Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza', 'naranja']

#### Eliminar un elemento por su índice
    del mi_lista[1]  # Elimina 'banana'
    print(mi_lista)  # Imprime ['manzana', 'cereza', 'naranja']

#### Eliminar un elemento por su valor (solo el primero que coincida)
    mi_lista.remove('naranja')  # Elimina 'naranja'
    print(mi_lista)  # Imprime ['manzana', 'cereza']

#### Eliminar y devolver un elemento con pop()
    eliminado = mi_lista.pop(0)  # Elimina 'manzana' y lo guarda en la variable 'eliminado'
    print(eliminado)  # Imprime 'manzana'
    print(mi_lista)  # Imprime ['cereza']

### 5. Reemplazar todos los elementos de la lista

Si quieres reemplazar todos los elementos de la lista con nuevos valores, simplemente puedes asignar una nueva lista completa a la variable original.
Ejemplo:

    mi_lista = ['manzana', 'banana', 'cereza']

##### Reemplazar todos los elementos
    mi_lista = ['pera', 'kiwi', 'fresa']
    print(mi_lista)  # Imprime ['pera', 'kiwi', 'fresa']

Resumen de métodos para modificar listas:

    Modificar un solo elemento: mi_lista[índice] = nuevo_valor

    Modificar varios elementos (slicing): mi_lista[inicio:fin] = nueva_lista

    Agregar un elemento al final: mi_lista.append(valor)

    Agregar varios elementos al final: mi_lista.extend(lista)

    Insertar un elemento en una posición específica: mi_lista.insert(índice, valor)

    Eliminar un elemento por índice: del mi_lista[índice]

    Eliminar un elemento por valor: mi_lista.remove(valor)

    Eliminar un elemento y obtenerlo: mi_lista.pop(índice)

## ¿Cómo agrego elementos a una lista usando append()?

En Python, el método append() se utiliza para agregar un solo elemento al final de una lista. Es una forma sencilla y eficiente de añadir elementos a una lista sin modificar su estructura interna.

## ¿Cómo elimino elementos de una lista usando remove() y pop()?

### 1. remove(): Eliminar un elemento por valor

El método remove() elimina la primera ocurrencia de un valor específico en la lista. Si el valor no se encuentra en la lista, Python lanzará un error (ValueError).

### 2. pop(): Eliminar un elemento por índice y devolverlo

El método pop() elimina un elemento específico por su índice y devuelve el valor eliminado. Si no se pasa un índice, pop() elimina y devuelve el último elemento de la lista.

Diferencias clave entre remove() y pop():

   1 remove():

        Elimina un valor específico.

        Solo elimina la primera ocurrencia del valor.

        No devuelve nada, solo elimina el valor.

        Lanza un error si el valor no se encuentra en la lista.

   2 pop():

        Elimina un elemento por índice.

        Elimina el último elemento si no se especifica un índice.

        Devuelve el elemento eliminado.

        Lanza un error si el índice no es válido.
Resumen:

    remove(valor): Elimina la primera aparición de valor de la lista. Si no existe, lanza un ValueError.

    pop([índice]): Elimina el elemento en el índice especificado (por defecto, el último) y lo devuelve. Si el índice no existe, lanza un IndexError.

## Conocer la cantidad de elementos de una lista con len()

En Python, la función len() se utiliza para conocer la cantidad de elementos de una estructura de datos, como listas, cadenas, tuplas, diccionarios, entre otros.

len() te permite obtener la cantidad de elementos de una lista, cadena, tupla, diccionario, etc.

En el caso de las listas, devuelve la cantidad de elementos que tiene la lista.

En el caso de los diccionarios, devuelve la cantidad de claves (no los valores).

## Recorriendo listas con "for"

En Python, puedes recorrer (o iterar) una lista utilizando un bucle for. Esto te permite acceder a cada uno de los elementos de la lista de forma secuencial y realizar alguna operación con ellos.

Puedes recorrer la lista y modificar sus elementos. Sin embargo, para modificar directamente los elementos de la lista durante el recorrido, necesitarás usar el índice o hacer un recorrido por índices.

El bucle for es una forma sencilla de recorrer una lista y trabajar con cada uno de sus elementos.

Puedes usar for elemento in lista: para recorrer todos los elementos.

Si necesitas el índice de cada elemento, puedes usar enumerate().

## 🔵 Lógica de programación

### ¿Qué es un bucle anidado?

Un bucle anidado en Python es un bucle dentro de otro bucle. Esto significa que tienes un bucle for o while dentro de otro bucle for o while. Los bucles anidados se usan cuando necesitas realizar iteraciones múltiples o trabajar con estructuras de datos más complejas, como listas de listas o matrices.

Un bucle anidado es un bucle dentro de otro bucle.

Los bucles anidados son útiles para recorrer estructuras complejas como listas de listas (matrices).

Puedes usar bucles anidados con condiciones para realizar tareas más específicas, como filtrar elementos de una matriz.

### Cómo funcionan los índices y rangos en listas (range()).

En Python, los índices y los rangos son conceptos clave cuando trabajas con listas. El índice te permite acceder a un elemento específico de la lista, y el rango (usando range()) te ayuda a trabajar con secuencias de números, como cuando recorres una lista con un bucle for.

    Los índices te permiten acceder a los elementos de una lista. Los índices en Python comienzan en 0.

    Puedes usar índices negativos para acceder a los elementos desde el final de la lista.

    range() genera secuencias de números y se usa comúnmente en bucles for para recorrer listas por sus índices.

    El slicing te permite obtener sublistas usando rangos de índices.

### Introducción a las funciones: ¿qué es una función y por qué usarlas?

Una función en Python es un bloque de código reutilizable que realiza una tarea específica. Las funciones te permiten organizar y modularizar tu código, de modo que puedas evitar repetir código y hacerlo más limpio y fácil de mantener. Además, las funciones pueden tomar entradas (argumentos) y devolver salidas (valores de retorno), lo que las hace muy poderosas para realizar operaciones complejas de manera ordenada.

### ¿Por qué usar funciones?

  Reutilización del código: Las funciones te permiten escribir un bloque de código una vez y reutilizarlo tantas veces como necesites sin tener que duplicarlo.

  Modularización: Puedes dividir tu código en partes más pequeñas y manejables, lo que hace que tu programa sea más fácil de entender y mantener.

  Abstracción: Las funciones permiten abstraer detalles complejos, así que no tienes que pensar en lo que sucede dentro de la función cada vez que la usas. Solo te importa lo que hace y qué valores recibe y devuelve.

  Organización: Ayudan a mantener tu código limpio y organizado. En lugar de tener grandes bloques de código en un solo lugar, puedes agrupar funcionalidades relacionadas en funciones separadas.

  Mejor mantenimiento: Si necesitas cambiar algo en el comportamiento de tu programa, puedes hacerlo en una sola función, sin tener que buscar todas las instancias del mismo código repetido en diferentes lugares.

Las funciones en Python son bloques de código reutilizables que realizan tareas específicas.

Puedes definir funciones con la palabra clave def, y estas pueden recibir parámetros y devolver resultados con return.

Las funciones permiten modularizar y organizar el código, haciendo que sea más fácil de mantener y reutilizar.

### ¿Por qué se definen funciones con def?

#### ¿Qué hace def?

Le dice a Python: “Estoy creando una función”.

Después de def, se pone el nombre de la función.

Luego vienen los paréntesis (donde van los parámetros, si los hay).

Y por último, dos puntos : para indicar que empieza el bloque de código de la función.

### ¿Qué es llamar(usar) funciones?

Llamar una función significa usar una función que ya definiste (o que ya existe).

Ejemplo básico:

Primero definimos una función:

    def saludar():
    print("Hola, ¿cómo estás?")
Aquí no se ejecuta la función todavía, solo la creamos.

Ahora vamos a llamarla (usarla):

    saludar()
Cuando escribes saludar():

Python busca esa función.

Ejecuta el código que tiene dentro (print("Hola, ¿cómo estás?")).

### ¿Qué son los parámetros y argumentos de una función?

Los parámetros son variables que defines dentro de los paréntesis al crear una función. Sirven como entrada para que la función pueda trabajar con diferentes valores.

    def saludar(nombre):  # <-- "nombre" es un parámetro
    print("Hola", nombre)

Los argumentos son los valores reales que pasas a la función cuando la llamas.

    saludar("Ana")  # <-- "Ana" es un argumento

#### ¿Por qué es útil?

Los parámetros hacen que las funciones sean flexibles. En lugar de hacer una función para cada caso, puedes pasarle diferentes argumentos y reutilizar el mismo código.

### ¿Qué es el retorno de una función 'return'?

El return sirve para que una función devuelva un resultado que puedas usar después. No solo hace algo (como imprimir), sino que te da un valor de vuelta.

    def sumar(a, b):
    return a + b
Aquí la función devuelve el resultado de la suma.
Pero nada se imprime en pantalla todavía.

Ejemplo:
       
    resultado = sumar(3, 4)
    print("La suma es:", resultado)
    sumar(3, 4) devuelve 7.

Ese 7 se guarda en la variable resultado.

Luego lo imprimes.

_Esta página está en construcción..._
