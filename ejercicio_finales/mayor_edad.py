#!/usr/bin/python3


def mayor_edad(edad):
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Eres menor de edad")

def main():
    edad = int(input("Ingresa tu edad: "))
    mayor_edad(edad)


if __name__=="__main__":
    main()
