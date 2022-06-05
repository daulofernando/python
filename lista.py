#!/usr/bin/env python3

users = []
users.append("daulo")

users.insert(1, "fernando")
users.insert(2, "ribeiro")
users.append("botelho")

lista = []
lista.insert(0, "carro")
nova_lista = lista + users # cria uma lista com duas listas
print(nova_lista)
head, *body, tail = users

users.extend(outra_lista) # adiciona uma lista a outra modificando a original

print(users)

users.remove("fernando")
users.pop() # tira o ultimo da lista

print(users)

print(head,body,tail)