#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: Christian Rebischke 
# Numerik 1 Grundlagen der Numerik

import time
from numpy import array, random

def NormInfty(A):
  m = A.shape[0] # Anzahl Zeilen
  n = A.shape[1] # Anzahl Spalten
  norm = 0
  tmp = []
  tmp2 = []
  for i in range(0, m):
    for element in A[i]: #Einzelne Elemente jeder Zeile
      tmp.append(abs(element)) #|element|
    tmp2.append(sum(tmp)) #|element1| + |element2|....
    #print("sum of ",tmp)
    tmp = []
  norm = max(tmp2) #Maximum ermitteln
  return norm

def Norm1(A):
  m = A.shape[0] # Anzahl Zeilen
  n = A.shape[1] # Anzahl Spalten
  norm = 0
  tmp = []
  tmp2 = []
  for i in range(0,n):
    for element in A[:,i]: #Einzelne Elemente jeder Spalte
      tmp.append(abs(element))
    tmp2.append(sum(tmp))
    #print("sum of ", tmp)
    tmp = []
  norm = max(tmp2)
  return norm

n = 100
#A = random.rand(n,n)
# Test mit einfachen Zahlen
A = __import__("numpy").arange(15).reshape(3, 5)
print("l1-Norm: %e Unendlichnorm: %e" % (NormInfty(A),Norm1(A)))
