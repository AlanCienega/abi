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
## ¿Por qué programar con Abi?

La diferencia con otros lenguajes en español es que este no "traduce" las palabras reservadas tipicas de los lenguajes, sino que estas se integran directo en las frases para sonar de manera lógica tal que se pueda entender  lo que hace el lenguaje incluso sin tener que escribir, alguien simplemente te puede contar lo que esta leyendo y al final sabes donde y que valores toman las entidades que te estan contando 

Es mucho mas facil entender y guardar en la memoria (humana)

```
a mi_edad asignale 20
```
que retener "mi_edad menor menos 20"
```
mi_edad <- 20
```
tambien podrias pensar en "mi_edad flecha izquierda 20"

pero al final, te quedarias con que mi_edad vale 20 porque sabes que se le ha asignado ese valor, puesto que ya es una frase no tienes que aprender un lenguaje de programacion, sino que ya saabes un lenguaje, ESPAÑOL, ahora solo te faltaria saber programar pero en gran parte tambien ya lo sabes, le das valores a las cosas y tambien las modificas, entonces una vez que aprendas a hacer operaciones basicas con este lenguaje, estaras listo para dar el salto a cualquier otro lenguaje de programación

### Comparación de ciclos
Los loops (ciclos) en programación simplemente son repeticiones de algo n cantidad de veces


<b>Ciclo en otro lenguaje en español</b>
```
Para i <- 1 Hasta 5 Hacer
  Escribir "Hola Mundo"
FinPara
```

<b>Ciclo en Abi</b>
```
repite:  muestra "hola Mundo" 5 veces
```
En el español los dos puntos ":" se usan como ejemplificacion del resto del contenido.

Por eso mismo cuando en Abi te encuentras con los dos puntos tu cerebro ya va a saber que lo que sigue es una accion derivada de la palabra que antecede los dos puntos.

Ejemplo: Esta misma linea es un ejemplo de ello.

En Abi
```
comentario: Esto solo lo va a leer el desarrollador, la maquina lo va a ignorar

repite: muestra "hola" 3 veces

ejecuta: unBloqueDeCodigo

```


## definicion de variables

Imagina que tienes carton para hacer cajas, la base es la misma, pero le debes poner una tapa con agujeros en forma de enteros o letras, NO AMBAS.
la tapa define el tipo de datos que le vas a poder meter a tu cajita

## Sintaxis

```
a tu_contenedor asignale 5
```

seria el equivalente a guardar un número entero 5 dentro un elemento llamado "tu_contenedor" y ahora ese elemento vale 5

## comentarios

inician con la palabra reservada "coemtario:" es importante los dos puntos no solo por sintaxis sino por emular correctamente el lenguaje

```
comentario: esto no lo va a interpretar el compilador, solo es para anotaciones
```

## declaracion de variables

en este lenguaje tienes que definir tu variable con un valor inicial con la palabra "asignale"

### números

```
comentario: inicializar enteros
a mi_edad asignale 0
```

### Booleanos o valores logicos

```
comentario: Inicializar booleanos
a tres_monitores asignale falso
```

## texto

Las cadenas de texto (strings), en la mayoria de lenguajes de programación se representan encerradas en comillas dobles, en el español se usan para  poner frases o citas, muy parecido pero ya que le das ese significado te va a hacer todo el sentido del mundo en los otros lenguajes.

```
a la_puerta asignale "negra"
```

### arreglos

```
comentario: define un arreglo
a las_tortillas asignale vacio

es como tener una caja con espacios para tortillas [   ] y este se encuentra vacio en un inicio
pero conforme le vas agegando cosa se va llenando

a las_tortillas agregale "azules"
a las_tortillas agregale "verdes"

ahora las_tortillas tendran este valor: ["azules", "verdes"]


```

## actualizar variables

para actualizar el valor es igual como cuando las declaras, de esta forma el valor que tenia si ya la habias declarado, entonces se va a reemplazar el valor

```
a mi_edad asignale 29
a mi_edad asignale 19
a mi_edad asignale 5

muestra mi_edad
```

## incremento y decremento de variables
se hacen con las palabras reservadas "agregale" y "quitale"
```
a monedas asignale 20
a monedas agregale 5
a monedas quitale 3

muestra monedas

comentario: la salida seria 22
```

## ¡También funciona con cdenas de texto!
```
comentario: si Alan tiene dos manzanas 
a manzanas asignale "dos"

comentario: Jesus le da mil
a manzanas agregale "mil"

comentario: Ana le quita dos
a manzanas quitale "dos"

comentario: pero José le dona 300
a manzanas agregale "trescientas"

comentario: y luego Yrvin se come mil
a manzanas quitale "mil"

comentario: ¿cuantas manzanas le quedan a Alan?

muestra "A Alan le quedan: "
muestra manzanas
muestra "manzanas"
```
Resultado en la terminal
```
A Alan le quedan: 
trescientas
manzanas
```
<h1 style="text-align:center; font-size: 500%"> 🤯 </h1>

Ten en cuenta que se quitan y ponen fragmentos de cadenas de texto mas no se convierte a numeros, veamos otro ejemplo:
```
a cancion asignale "un elefante se columpiaba sobre la tela de una araña"

a cancion quitale "araña"
a cancion agregale "señora que vendia telas"

muestra cancion
```
y como salida tendrias "un elefante se columpiaba sobre la tela de una señora que vendia telas"

## condicionales
Se usan como ya sabes usarlas.

si se cumple una condicion, procedes a mostrar lo que sucede.

es decir, tedrias que usar la palabra "si", luego un valor verdadero o falso dependiendo tu necesidad, seguido de una coma "," y entonces sigue la accion, veamos algunos ejemplo del uso real en el español:

Si tienes hambre, come.

Si tu telefono se romple, haz valida la garantía.

Si sabes escribir, ya sabes programar en Abi.

En codigo es bastante parecido:

```
a los_pollitos_tienen_hambre asignale verdadero

si los_pollitos_tienen_hambre, muestra "los pollitos dicen pio pio pio"

```
la salida del codigo al ejecutarlo seria
```
los pollitos dicen pio pio pio
```
pero si cambias el valor de los_pollitos_tienen_hambre a falso, entonces simplemente no obtendrias nada en el resultado de ejecutar el programa.

## Palabras reservadas

- agregale
- quitale
- a
- y
- o
- si
- no
- repite
- recorre
- veces
- arreglo
- cadena
- entero
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
a mi_edad asignale 29


bloque: restaTres años
  a mi_edad quitale años
fin



```

## resaltado de sintaxis abi
copia la carpeta abi-lenguaje-de-programacion--facilito- a donde estan instaladas tus extensiones
en linux algo asi:
```
└─$ cp -r abi-lenguaje-de-programacion--facilito- ~/.vscode/extensions

```
luego reinicia vscode
## glosario

- variables: Son como cajitas donde guardas cosas, en el lenguaje Abi solo enteros, letras, texto etc
