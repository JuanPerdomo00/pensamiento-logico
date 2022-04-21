#!/usr/bin/python3

def vela_encendida(r):
    if r == "si" or r == "s":
        print("La vela esta encendida")
    
    elif r == "no" or r == "n":
        print("Busca fosforos o un encendedor y prende la vela")
    else:
        print("Tienes una vela?")


def main():
    res = str(input("La vela esta encendida: si[s] o no[n]: "))
    vela_encendida(res)

if __name__=="__main__":
    main()
