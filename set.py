#!/usr/bin/env python3

# SET SEMPRE OMITE OS CARACTERES REPETIDOS

conjunto_a = set([1,2,3,4,5])
conjunto_b = set([4,5,6,7,8])

# SET DE ADIÇÃO
conjunto_a | conjunto_b 
conjunto_a.union(conjunto_b)

# SET DE INTERSEÇÃO
conjunto_a & conjunto_b 
conjunto_a.intersection(conjunto_b)

# SET DE DIFERENÇA
conjunto_a - conjunto_b
conjunto_a.difference(conjunto_b)

# SET DE DIFERENÇA SIMETRICA
conjunto_a ^ conjunto_b
conjunto_a.symmetric_difference(conjunto_b)