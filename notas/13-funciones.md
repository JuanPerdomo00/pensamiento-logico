# ¿Qué es una función?

Son bloques de codigo que realizan una actividad especifica.

## Para que nos sirven las funciones y cual es su mejor implementacion

**sirven para: **
- Modulizar
-  Optimizar
-  Organaizar
-  Encapsular

Imaginemos a la **declaración de la función** como la creación de una plantilla de código que podrás usar después, declarar una función no es más que simplemente escribir que va a hacer:

```js
function decirHola() {
    imprime "Hola!!"
}
```

Listo, ya tenemos la función declarada, sin embargo, ese código por sí solo no hace nada, tenemos que decirle que haga algo, ¿cómo lo hacemos? ¡Mandándola a llamar!, para mandar a llamarla simplemente escribimos su nombre con un par de paréntesis:

```js
decirHola()
```

¡Listo!, la mandamos a llamar, esto va a imprimir **“Hola!!”**, ahora, ¿que pasaría si la mandamos a llamar dos veces?

```js
decirHola()
decirHola()
```

Si dijiste que va a imprimir dos veces **“Hola!!”** estás en lo correcto! Usando funciones podemos empezar a escribir código una sola vez y usarlo cuantas veces lo necesitemos, por eso se dice que las funciones nos permiten reutilizar código, el tema de las funciones es más amplio ya que también podemos retornar valores, por ejemplo:

```js
function suma() {
    retorna 1 + 1;
}

variable x = suma()
```

En este caso, podemos ver que la función se está mandando a llamar justo al lado de una varaible, recuerda que al usar variables es como tener cajitas o canastas, cualquier cosa que devuelva `suma()` se va a guardar ahí dentro de esa “`x`”, sin embargo, aquí la palabra clave es ese “retorna” que está dentro de la declaración función, porque eso es lo que especifica que se tiene que devolver algo, en este caso, una suma, por tanto podemos intuir que “`x`” va a contener el valor del resultado de `1 + 1` 
.  
También podemos pasar parámetros:

```js
function suma(x, y) {
    retorna x + y;
}

variable x = suma(2, 1)
```

Y seguramente ya estás intuyendo que “`x`” equivale a 2 y “`y`” equivale a 1 y así es, los argumentos se pasan dependiendo de la posición en la que los parámetros fueron escritos, es decir, si el primer argumento es “2” entonces ese valor le correponde a “`x`”, si el segundo algumento es “1” entonces ese valor le corresponde a “`y`” y así sucesivamente 
