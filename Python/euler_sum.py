#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 
# Euler-Funktion auf Basis von Summen
# von Christian Rebischke 

import math

def fac(x):
  if x == 1:
    return 1
  else:
    return x * fac(x-1)

# Initialisiere variablen
n = 1
last = 0
current = 0

# Erstelle Array mit 1 wegen 1 + Sum...
array = [1]

while True:
  factor = 1 / fac(n)
  array.append(factor)
  current = sum(array)
  print("%s. Durchlauf: %s" % (n,current))
  # Breche ab wenn letzter und vorletzter eintrag gleich sind
  if last == current:
    break
  last = current  
  n += 1
    

print("Der absolute Fehler beträgt:", abs(current-math.e))
print("Der relative Fehler beträgt:", abs(current-math.e) / current)

