# Abi Lenguaje de Programación

## El lenguaje para que de una vez por todas aprendas a programar

Basado en el lenguaje natural del español mexicano, y listo para que hasta un bebé pueda aprender, tenemos un lenguaje que hace exactamente lo que le estas escribiendo.

## Hola mundo en Abi

```
muestra "Hola mundo"
```

la salida de ejecutar el codigo.abi seria

```
Hola mundo
```

## definicion de variables

Imagina que tienes carton para hacer cajas, la base es la misma, pero le debes poner una tapa con agujeros en forma de numeros o letras, NO AMBAS.
la tapa define el tipo de datos que le vas a poder meter a tu cajita

## Sintaxis

```
a tu_contenedor tipo numero asignale 5
```

seria el equivalente a guardar un numero 5 dentro un elemento llamado "tu_contenedor" y ahora ese elemento vale 5

## comentarios

inician con la palabra reservada "coemtario:" es importante los dos puntos no solo por sintaxis sino por emular correctamente el lenguaje

```
comentario: esto no lo va a interpretar el compilador, solo es para anotaciones
```

## declaracion de variables

en este lenguaje tienes que definir tu variable con un valor inicial con la palabra "asignale" ademas tienes que definir el tipo, esto ayuda a que puedas acceder a operaciones validas para el tipo de dato

### números

```
comentario: inicializar numeros
a mi_edad tipo numero asignale 0
```

### Booleanos o valores logicos

```
comentario: Inicializar booleanos
a tres_monitores tipo logico asignale falso
```

## texto

```
a la_puerta tipo texto asignale "negra"
```

### arreglos

```
comentario: define un arreglo
a las_tortillas tipo arreglo asignale vacio
comentario: en python equivale a; las_tortillas = []
comentario: para agregar algun elemento al arreglo:
a las_tortillas agregale "blancas"
a las_tortillas agregale "azules"
comentario: en python ya tendriamos esto en las_tortillas:

["blancas", "azules"]
```

## actualizar variables

para actualizar su valor ya no tienes que escribir el tipo pues se tomaria como nueva declaracion y daria error

```
a mi_edad asignale 29
```

## condicionales

```
a la_puerta tipo texto asignale "negra"
a hay_cien_candados tipo logico asignale verdadero

si la_puerta es "negra" y hay_cien_candados
  muestra "van a poder a mi detenerme"

```

## Palabras reservadas

- agregale
- quitale
- a
- en
- y
- o
- si
- no
- repite
- recorre
- veces
- tipo
- arreglo
- cadena
- numero
- logico
- verdadero
- falso
- vacio
- comentario:

Nota que en el español tienes conectores como "a", "en", "de" que muchas veces no notamos pero son de las cosas mas utiles para poder darle lógica a la oracion que estas armando, para este lenguaje ademas de funcionar como conector, tambien marcan sintaxis valida de ABI, tomemos como ejemplo "a mi_variable agregale 5":

el equivalente de "a mi variable" seria "variable = " que entendemos que sera una asignación, siempre que aprendes un lenguaje te confundes con el "=" porque piensas que es una evaluación y normalmente se tarda en acostumbrarse a mentalziar que en realidad es una asignacion, por eso con un aletra "a" nos hace mas sentido que vamos a hacer algo con la cosa que sigue.

## soporte para ciclos

podrias recorrer un arreglo, recordemos que a las_tortillas le agrgamos dos valores

### recorre (para arreglos)

```
recorre las_tortillas y muestra la_tortilla
```

En python:

```
for la_tortilla in las_tortillas:
  print(la_tortilla)
```

Observemos que nuestra "funcion" recorre, no nos define a la_tortilla en la declaracion del ciclo, pero podemos acceder a ella en el final de la sentencia debido a una declaracion interna del lenguaje que hace mas facil la lectura.

ademas los delimitadores del ciclo "recorre" y "y" envuelven al arreglo que vamos a recorrer, luego viene la accion y finalmente la variable anonima (al menos hasta que le pongas nombre)

Internamente el lenguaje crea una variable que no tiene nombre hasta que accedes a ella, en este caso definimos por convension y debido al contexto a "la_tortilla" pero pudimos haber escrito cualquier nombre

```
recorre: las_tortillas y muestra un_perro
```

como resultado seguiria nostrandonos

```
blancas
azules
```

## repite (ciclo for)

```
repite: muestra "Hola" 5 veces
```

como salida tendriamos

```
"hola"
"hola"
"hola"
"hola"
"hola"
```

aunque parece mas facil escribir simplemente

```
muestra "hola" 5 veces
```

la palabra reservada "repite", de nuevo es un gran delimitador que ademas marca una correcta sintaxis, que ademas nos indica lo que hay que hacer con lo que sigue.

## funciones sin parametros

las funciones o bloques son fragmentos de codigo que van a encapsular funcionalidades, asi si queremos hacer eso varias veces en lugar de repetir el codigo, mandamos a llamar a la funcion

```
bloque: saludo
  muestra "Hola desde:"
  muestra "un bloque"
fin

ejecuta: saludo

```

la salida seria;

```
Hola desde
un bloque
```

## funciones con parametros

Este tipo de funciones tienen su nombre y las palabras que siguen serian valores que acepta para poder realizar una operacion

```
a mi_edad tipo numero asignale 29


bloque: restaTres años
  a mi_edad quitale años
fin



```

## glosario

- variables: Son como cajitas donde guardas cosas, en el lenguaje Abi solo numeros, letras, texto etc
