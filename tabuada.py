#!/usr/bin/env python3

numeros = list(range(1,11))

for numero in numeros:
    print("{:-^20}".format(f" Tabuada do: {numero} "))
    print("-"*20)
    for outro_numero in numeros:
        operador=(f'{numero}x{outro_numero}')
        operacao=(numero*outro_numero)
        print("{:^20}".format(f'{operador} = {operacao}'))
    print("-"*20)