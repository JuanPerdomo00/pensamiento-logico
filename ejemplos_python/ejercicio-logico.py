#!/usr/bin/python3

banco_cliente = str(input("Ingresa el nombre del banco: "))
cuenta_cliente = int(input("Cuanto tienes en la cuenta: "))
banco_destino = str(input("A cual banco vas a transferir: "))
hora_transferencia = int(input("a que horas estas tranfiriendo: "))
cuenta_destino = cuenta_cliente
saldo_cliente = 0


if banco_cliente and banco_destino:
    if banco_destino == banco_cliente or banco_cliente == banco_destino:
        if hora_transferencia == 9 or hora_transferencia >= 12 or hora_transferencia == 15  or hora_transferencia >= 20:
            cuenta_destino = cuenta_cliente
            saldo_cliente = cuenta_destino
            print(f"Tu saldo es: {saldo_cliente}")
        else:
            print("Ya serramos")
    elif banco_cliente != cuenta_destino or banco_destino != banco_cliente:
        cuenta_destino = cuenta_cliente - 100
        saldo_cliente = cuenta_destino
        print(f"Tu saldo es: {saldo_cliente} se te agrego cobro costo de transaccion")
else:
    print("Error")        
