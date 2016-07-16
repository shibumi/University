#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Christian Rebischke 
#
# Die Kleinste positive Zahl kann man mit print(numpy.finfo(numpy.float64).tiny)
# ermitteln. Für die anderen Datentypen ist dies äquivalent.
#
# Größte positive Zahl bei Float mit der man 1.0 erreicht: 1.11e-16
# Kleinste positive Zahl bei Float mit der man 1.0 erreicht: 2.22507385852e-308
#
# Kleinste positive Zahl bei Float32 mit der man 1.0 erreicht: 1.17549e-38
# Die Größte konnte ich nicht ermitteln..
#
# Größte positive Zahl bei Float mit der man 1.0 erreicht: 1.11e-16
# Kleinste positive Zahl bei Float mit der man 1.0 erreicht: 2.22507385852e-308
#
#


try:
  from numpy import float32, float64

except ImportError:
  print("Please install numpy")



x = float(input("Please insert a float number.. x = "))
y = float32(input("Please insert a float32 number.. y = "))
z = float64(input("Please insert a float64 number.. z = "))

print("%1.16f" % x)
print("%1.16f" % y)
print("%1.16f" % z)


x = x + float(1)
y = y + float32(1)
z = z + float64(1)

print("%1.16f" % x)
print("%1.16f" % y)
print("%1.16f" % z)

