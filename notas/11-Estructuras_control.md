# If y Else: condicionales y comparaciones para proteger tus algoritmos

## Estructuras de control:

Herramientas sobre las cuales se construye un algoritmo. Nos ayudan a construir el flujo de nuestras tareas.

## If/Else:

Si se cumple determinada condición se ejecuta acción/código anidada en el `if`, si no es así se ejecutará la anidada en el `else`. Esta es muy usada para validar información.

```python
# If Else en python

x = 10

if x < 20: # como x vale 10 entra ala condicion, caso contrario entraria al else
	return "Me ejecuto"
else:
	return "no me ejecuto" 
```


# Switch y Case: condicionales en forma de casos

## Qué es Switch y Case

Es una estructura de control, que nos permite evaluar múltiples casos que puede llegar a cumplir una variable y realizar una acción en esa situación.

## Estructura del condicional switch.


![](https://i.imgur.com/lhD4YK0.png)

```c
#include<stdio.h>
int main() {
	char ch;

	printf("Introduzca una vocal: "); 
	ch=getchar();  	
	switch(ch) {
		case 'a': puts("Se ha pulsado una a.");
			break;
		
		case 'e': puts("Se ha pulsado una a.");
			break;

		case 'i': puts("Se ha pulsado una a.");
			break;

		case 'o': puts("Se ha pulsado una a.");
			break;

		case 'u': puts("Se ha pulsado una a.");
			break;

		default: puts("Error");

		}
	return 0;
}
```

# Excepciones y errores: Throw y Try Catch
## Qué son las excepciones

Son eventos anormales que ocurren durante la ejecución **(no funciona como un else)**.

-   `throw`: es una herramienta que podemos invocar en cualquier punto nos permite capturar si funciona o no lo que se ejecutó**.**
    
-   `try ... catch`: intenta hacer X, pero, si falla haz Y.
    
-   `finally`: sucede después del `try y catch`.
    

Estas estructuras son solo para errores de ejecución, no de lógica.

```python
# try catch
try:
	print(x)
except err as e:
	print("Todo va estar bien")
	
finally:
	print("Todo va estar bien")

```


# ¿Qué es un ciclo? While, For y Do While
## ¿Qué es un ciclo?

Es una estructura de control que ejecuta un bloque de instrucciones de manera repetida.

###### ¿Cuándo utilizar un ciclo `for`, `while` o `do while`?

-   **For:** cuando sabes (o puedes saber) las veces repetirás el ciclo. **Ejemplos:** “5 veces”, “la cantidad de elementos que tiene un arreglo”.
    
-   **While:** Cuando no sabes las veces que se repetirá un ciclo. **Ejemplos:** “reintentar conectarme a una base de datos si falló al hacerlo”
    
-   **Do While:** Cuando no sabes las veces que se repetirá un ciclo y necesitas que se realice por lo menos una vez. **Ejemplos:** “Conectarme a la base de datos, si falló, repetir hasta que me pueda conectar”

![](https://i.redd.it/6wksqjmmyw321.jpg)

- **While python**
```python
# bucle while en python
numero = 0

while numero < 10:
	print(f"Numero es {numero}")
	numero += 1
```
resultado
```
Numero es 0!
Numero es 1!
Numero es 2!
Numero es 3!
Numero es 4!
Numero es 5!
Numero es 6!
Numero es 7!
Numero es 8!
Numero es 9!
```

for en c
```c
#include<stdio.h>

int main() {

	for (x = 0; x < 10; x++) {
		printf("%x", x);
	}
	
	return 0;
}

```

resultado
```
EL numero x es: 0 
EL numero x es: 1 
EL numero x es: 2 
EL numero x es: 3 
EL numero x es: 4 
EL numero x es: 5 
EL numero x es: 6 
EL numero x es: 7 
EL numero x es: 8 
EL numero x es: 9 
```

do while en c
```c
#include <stdio.h>

int main() {
	int x = 10;
	
	do {
		printf("EL valor de x es: %x \n", x);
		x++
		}
	while(x < 20);
	
	return 0;
}
```

