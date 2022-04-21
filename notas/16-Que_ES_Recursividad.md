# ¿Qué es recursividad? Funciones que se llaman a sí mismas

## ¿Qué es la recursividad?

Son funciones que se llaman a sí mismas en el momento que se están ejecutando. Es muy importante tener en cuenta que las debemos controlar para que no caigan en un _loop_ infinito y no rompan el flujo normal de nuestra aplicación.

## La mejor forma de trabajar con la recursividad:

Lo mejor es condicionarlas, para que solo se llamen a sí misma bajo una condición que tenga un fin y que luego de ese fin el flujo de la aplicación pueda continuar normalmente.


### Recursividad en python
```python
#!/usr/bin/python3

def cuenta_regresiva(n):
    n -= 1 

    if n > 0:
        print(n)
        cuenta_regresiva(n)
    else:
        print("Feliz Feliz")


def main():
    n = int(input("Ingresa un numero: "))
    cuenta_regresiva(n)


if __name__ == "__main__":
    main()
```