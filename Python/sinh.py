#!/usr/bin/env python
#-*- coding: utf-8 -*-
# 
# von Christian Rebischke 

"""
In welchem ungefähren Bereich x ≥ 0 vermuten Sie, ist die naive Auswertung
genauer als die Taylor Approximation?
Begrunden Sie Ihre Antwort.

Antwort:
Umso näher x an 0 annähert umso genauer ist die Taylor-Approximation.
Umso größer x umso genauer ist der naive Ansatz mit der exponentialfunktion.

Der naive Ansatz wird also mit kleinerem x ungenauer weil e^x und e^-x bei
kleinerem x sich immer mehr annähern. Dadurch, dass x dargestellt wird als
floatingpoint number wächst auch der Verlust der Genauigkeit. 
Dieses Verhalten nennt sich 'cancellation' oder auch das Prinzip der
'Auslöschung'. Es kommt dadurch zustande, dass die niedrigwertigen Stellen
beispielsweise durch Rundungsfehler beeinflusst worden sind. Dies hat zur Folge
das wenn die höherwertigen Stellen übereinstimmen, dass sich die gültigen
Stellen zu 0 rauslöschen.

Meine Vermutung stimmt also überein. Je kleiner man x wählt umso größer ist der
Verlust der Genauigkeit bei dem naiven Ansatz

"""
try:
  import math
  from numpy import float32, float64

except ImportError:
  print("Bitte istallieren Sie numpy")
    
#print("Der absolute Fehler beträgt:", abs(current-math.e))
#print("Der relative Fehler beträgt:", abs(current-math.e) / current)

# Input
x = float64(input("Bitte geben Sie ein x >= 0 an: "))

# Berechnungen
sinh_naiv = float64(((math.e**x)-(math.e**(-x)))/2)
sinh_taylor = float64(x + ((x ** 3) / 6))
sinh_math = (math.sinh(x))

# Ausgabe der Ergebnisse
print("sinh mit dem naiven Algorithmus ist: ", float64(sinh_naiv))
print("sinh mit dem taylor ansatz ist: ", float64(sinh_taylor))
print("sinh aus der math library ist: ", float64(sinh_math))


# Absoluter und relativer Fehler berechnen
print("Der Absolute Fehler für den naiven Ansatz ist: ", abs(float64(sinh_naiv-sinh_math)))
print("Der relative Fehler für den naiven Ansatz ist: ", abs(float64((sinh_naiv-sinh_math) / sinh_naiv)))


print("Der Absolute Fehler für den taylor Ansatz ist: ", abs(float64(sinh_taylor-sinh_math)))
print("Der relative Fehler für den taylor Ansatz ist: ", abs(float64((sinh_taylor-sinh_math) / sinh_taylor)))
