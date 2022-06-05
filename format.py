#!/usr/bin/env python3
print("metodo 1:")
nome = "daulo"
num = 1
pontos = 100.345
msg = ("olá %s você é o player nº %03d e possui %.2f pontos" % (nome,num,pontos))
print(msg)

print("-"*13)

print("metodo 12: format string")
msg = "olá {nome} você é o player nº {num:03d} e possui {pontos:.2f} pontos"
print(msg.format(nome="daulo",num=1,pontos=100.345))

print("-"*13)

print("metodo 23: f string")
nome = "daulo"
num = 1
pontos = 100.345
print(f"olá {nome} você é o player nº {num:03d} e possui {pontos:.2f} pontos")

print("\U0001F43C") # imprimindo emoji unicode
print("\N{PANDA FACE}") # imprimindo emoji unicode
