#!/usr/bin/env python3

sala1 = ["Eric","Maia","Gustavo","Manuel","Sofia","Joana"]
sala2 = ["Joao","Antonio","Carlos","Maria","Isolda"]

aula_ingles = ["Eric","Maia","Joana","Carlos","Antonio"]
aula_musica = ["Eric","Carlos","Maria"]
aula_danca  = ["Gustavo","Sofia","Joana","Antonio"]

atividades = [("Inglês",aula_ingles), ("Música",aula_musica), ("Dança",aula_danca)]

for nome_atividade, atividade in atividades:

    atividade_sala1 = []
    atividade_sala2 = []
    
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"Alunos da aula de {nome_atividade} da sala 1",atividade_sala1)
    print(f"Alunos da aula de {nome_atividade} da sala 2",atividade_sala2)