#!/usr/bin/python3

# cuentra regresiva con while
def con_while(n):
    while n > 0:
        print(n)
        n -= 1
    print("con while")

def con_recursividad(n):
    n -= 1

    if n > 0:
        print(n)
        con_recursividad(n)

    else:
        print("Con reculsividad")


def main():
    opcion = int(input("COn que hacer cuenta regresiva con 1.while o 2.recursivamente: "))
    if opcion == 1:
        num = int(input("Ingrese un numero donde empezar a contar: "))
        con_while(num)

    elif opcion == 2:
        num = int(input("Ingrese un numero donde empezar a contar: "))
        con_recursividad(num)

    else:
        print("Error")


if __name__=="__main__":
    main()
