#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 
# Euler-Funktion auf Basis von Limes
# von Christian Rebischke 

try:
  from sympy import limit, oo, Symbol
  x = Symbol("x")
  import math

except ImportError:
  print("Bitte istallieren Sie sympy")

# Initialisiere variablen
n = 1 
last = 0
current = 0


while True:
  current = limit(((1 + (1/n)) ** n), x, oo)
  print("%s. Durchlauf: %s" % (n,current))
  # Breche ab wenn letzter und vorletzter eintrag gleich sind
  if math.isclose(last, current, abs_tol=0.00000000000001):
    break
  last = current  
  n += 1
    
print("Der absolute Fehler beträgt:", abs(current-math.e))
print("Der relative Fehler beträgt:", abs(current-math.e) / current)
