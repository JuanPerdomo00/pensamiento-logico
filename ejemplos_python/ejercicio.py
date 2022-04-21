#!/usr/bin/python3

def cadena_trasnformar(letra):
    string = letra
    resul = ""

    for cadena in string:
        if cadena == cadena.upper():
            resul += cadena.lower()
        else:
            resul += cadena.upper()

    return resul


def main():
    cadena = str(input("Ingrese una cadena: "))
    print(cadena_trasnformar(cadena))

if __name__ == "__main__":
    main()