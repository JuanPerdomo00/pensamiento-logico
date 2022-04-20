#/usr/bin/python3
from datetime import *



day = date.today()

def comprar_tiketes():
    # capasidad de los madios de transporte
    capasidad_bus = 50
    capasidad_avion = 200
    numeros_asiento_avion = 200
    numeros_asiento_bus = 50
    tiket = str(input("Quie medio de transporte desea tomar avion[v] o bus[b]: ")).lower()

    if tiket == "v" or tiket == "avion":
        ciudad_origen = str(input("Ciudad de origen: "))
        ciudad_destino = str(input("Ciudad Destino: "))
        cantidad_puestos = int(input("Cuantos boletos va comprar: "))

        if numeros_asiento_avion - cantidad_puestos <= 0:
            print(f"El avion no cuenta con asientos disponibles, #numero asientos disponibles {numeros_asiento_avion}")
        else:
            numeros_asiento_avion -= cantidad_puestos
            datos_pasajero = str(input("Ingrese su nombre completo: ")).capitalize().replace(" ", ",")
            fecha = day
            # hora = date.hour + date.minute + date.second
            print(f"""
                Compra exitas

                Nombre pasajero: {datos_pasajero}

                Fecha y hora de compra: {fecha}

                Ciudad de origen: {ciudad_origen}

                Ciudad destino    {ciudad_destino}
                  """)
    elif tiket == "b" or tiket == "bus":
        ciudad_origen = str(input("Ingrese ciudad origen: "))
        ciudad_destino = str(input("Ingrese ciudad destino: "))

        cantidad_puestos = int(input("Cuantos boletos va comprar: "))
        datos_pasajero = str(input("Ingrese su nombre completo: ")).capitalize()
        #fecha = date.year + date.month + date.day
        #hora = date.hour + date.minute + date.second

        if tiket != 1 and tiket != 2:
            print("Datos incorrectos")


def main():
    comprar_tiketes()


if __name__=="__main__":
    main()
