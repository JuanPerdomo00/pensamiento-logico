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