# Que es el sistema bianrio
El **sistema binario** es un sistema de numeracion que esta que esta representado por estas dos cifras: **0** y **1**. La cuales representan duferentes valores cuando hay carga, cuando no hay carga, cuando hay energia, cuando no hay energia, que es el quivalente a 1 y 0.

En este caso de nuestro ejemplo tenemos un bombillo encendido, el cual representa un 1 y el bobillo apagado el cual representa el 0. Nuestro sistema binario tambien nos puede representar el positivo + y el negativo -, el True o el False. Y todo esto siempre va ir conectados con nuetros 1 y 0, que es la representacion de este sistema numerico.

![](https://i.imgur.com/rlX67i7.png)

Con este sistem,a de numeracion podemos hacer tambien operaciones aritmeticas tal como lo hariamos con el sistema decimal.

## Ejemplo
Dividamos de cada dos en dos, cada unos de los resulrados y vamos a guardar nuestro valor restante. Lo primero que vamos hacer es tener en cuenta que el 34 es un numero par, por lo tanto, lo vamos a dividir entre dos y no nos vamos a tener ningun valor resultante asi que sera `34 / 2 = 17 (queda 0`

Ahora vamos a tomar nuestro valor.

17 y lo vamos a dividir entre dos.  
`17 / 2`

Pero aquí tenemos un detalle 17 no es un número par, así que vamos a dividirlo entre dos, nos quedaría un resultado de 8 y nos queda un resultante 1. Por lo tanto, si multiplicó 8 por 2, me daría 16 y tendría un una unidad adicional para llegar al número 17.

`17 / 2 = 8` (queda 1)

Nuevamente, tomamos el valor 8 y lo dividimos entre 2.

8 es un número par y el resultado es 4. En consecuencia, es un resultado exacto y nuevamente ya no nos va a quedar ningún valor, así que nos quedaría cero.

`8 / 2 = 4` (queda 0)

Y si multiplicamos 4 por 2, tendríamos 8 de manera exacta.

Tomemos 4 nuevamente y lo dividimos entre 2. Vamos a tener un resultado par que es el número 2 y nos queda nuevamente un valor cero.

`4 / 2 = 2` (queda 0)

Ahora vamos a tomar el 2 y lo vamos a dividir entre 2. Vamos a tener un resultado igual a 1 y nuevamente lo que nos queda es cero.

`2 / 2 = 1` (queda 0)

Tomamos 1 lo dividimos entre 2 y vamos a tener cero. Para llegar a 1, necesitaríamos una unidad y hasta aquí podríamos llegar con nuestra conversión, porque de aquí en adelante ya no podríamos seguir dividiendo entre dos.

`1 / 2 = 0` (queda 1)

Ahora, ¿dónde está el número binario que representa el 34 en número decimal?

Pues, lo que vamos a hacer es tomar nuestro último resultante y vamos a ir hasta el primero solo en la lista de resultantes. De esta forma, nuestro valor 34 en número Binario es igual a 100010

Y esta es la forma correcta de leerlo y de interpretarlo. Si estuviéramos pensando en sistema decimal a lo mejor podríamos decir que su número es cien mil diez, pero esta no sería la forma adecuada. La manera adecuada es leerlo con sus uno y cero. 100010 iguales a 34 que es un número decimal

## Operaciones Aritméticas

### Suma

Para sumar debes tener en cuenta 4 arreglos posibles: `0 + 0 = 0`; `0 + 1 = 1`; `1 + 0 = 1`; `1 + 1 = 10`. Por lo tanto, el resultado de sumar `1 0 0 1 1 0 0 0` y `0 0 0 1 0 1 0 1` es `1 0 1 0 1 1 0 1`

### Resta

Para llevar a cabo una resta también hay 4 combinaciones posibles: `0 - 0 = 0`; `1 - 0 = 1`; `1 - 1 = 0`; `10 - 1 = 1`. Si restas los mismos números que usamos para la suma quedaría de la siguiente forma: `1 0 0 1 1 0 0 0 - 0 0 0 1 0 1 0 1 = 1 0 0 0 0 0 1 1`

### Acarreo

Si lo notaste, hay dos casos especiales en los que utilizamos más de un dígito: `1 + 1 = 1 0` y `1 0 - 1 = 1`. Esto se debe al acarreo y es algo que ya conoces del sistema decimal, la diferencia es que en el sistema binario también se puede acarrear de manera negativa.

La resta de `0 - 1` no es posible, es por esto que el `0` pide la ayuda de su compañero de la izquierda y le quita un `1` que le permite realizar la operación. Entonces, el `0` que pidió prestado se convierte en `1 0` y al restarle `1` nos da como resultado `1 0 - 1 = 1`. El compañero que tenía a su izquierda y le cedió el uno, por ende, va a perder ese uno y termina siendo un `0`. Si el compañero de la izquierda es un `0`, hará el mismo proceso de pedir valores a la izquierda hasta que un `1` pueda prestarles su valor.

Otra forma de verlo es que el resultado de la operación sería así: `1 0 - 1 = 1 1`. El resultado tiene dos `1` porque uno de ellos va a ser restado del dígito que está a la izquierda y prestó ese `1`.

### Multiplicación y división

Funcionan bajo las mismas condiciones que en el sistema decimal, todo número multiplicado por `0` es igual a `0` y solo es `1` cuando se multiplica por `1`.

![](https://static.platzi.com/media/user_upload/Curso%20B%C3%A1sico%20de%20Algoritmos%20y%20Pensamiento%20L%C3%B3gico-b6fac593-158b-4e5b-973e-6a07f7ff8876.jpg)