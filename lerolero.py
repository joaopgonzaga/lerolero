#!/usr/bin/python3
"""Gerador de lero-lero.

Gera frases de efeito sem significado real."""
import random

#Cada frase é composta por três partes aleatórias; aqui,
#listas de possibilidade para cada uma das partes.

parte1 = []
parte2 = []
parte3 = []

#Combina partes aleatoriamente
print(random.choice(parte1), random.choice(parte2), random.choice(parte3))
