#!/usr/bin/python3
import time

def crear_cuenta():
    pass

def cobrar():
    valor_unitario = 1000000
    valor_total = valor_unitario


def main():
    validar_cuenta = str(input("TIene cuenta? si[s] o no[n]: "))

    if validar_cuenta == "si" or validar_cuenta == "s":
        nombre_c = str(input("Deme su nombre: "))
        cantidad_prendas = int(input("Cantidad de prendas: "))
        tipos_prendas = str(input("Tipos de prendas: "))

    elif validar_cuenta == "no" or validar_cuenta == "n":
        print("No tiene cuenta...")
        time.sleep(.1)
        crear = str(input("Desea crear cuenta de cobro si[s] o no[n]: "))
        if crear == "si" or crear == "s":
            crear_cuenta()
        elif crear == "n" or crear == "no":
            print("")
        
        

if __name__=="__main__":
    main()