#!/usr/bin/env python
# Etwas Spass mit Graphen..

# Graph aus Aufgabe 4.1
G = { 'A': ['B', 'C'],
      'B': ['C', 'D'],
      'C': ['D'],
      'D': []}

# Weiterer Beispielgraph
T = { 'A': [],
      'B': ['D'],
      'C': ['C', 'A'],
      'D': ['C','A']}

def countNodes(A):
    """
    countNodes - zählt die Anzahl der Knoten
    Diese Funktion zählt ganz stupide die Anzahl der Knoten.
    """
    nodes = 0
    for i in A:
        nodes += 1
    return nodes

def countArrows(A):
    """
    countArrows - zählt die Anzahl der gerichteten Kanten
    Diese Funktion zählt einfach ganz stupide die Anzahl
    aller Kanten. Wenn ich eine antiparallele Kante habe,
    also eine Kante die in 2 Richtungen geht zwischen 2 Knoten
    zählt diese in diesem Algorithmus als 2 Kanten. Wenn man
    will, dass diese nur als eine Kante zählt kann man
    countEdges benutzen.
    """
    baseCount = 0
    for i in A:
        baseCount += len(A.get(i))
    return baseCount

def countEdges(A):
    """
    countEdges - zählt die Anzahl der ungerichteten Kanten
    Mit dieser Funktion kann man die Anzahl der ungerichteten
    Kanten zählen. Dabei ist eine ungerichtete Kante zwischen
    2 Knoten als _EINE_ Kante gezählt. Es werden also
    praktisch nur die Striche zwischen den Knoten gezählt.
    Der Algorithmus tut nichts anderes als aus einem
    gerichteten Graphen einen Ungerichteten machen und 
    zählt dann die Anzahl der gerichteten Kanten.
    """
    B = A.copy()
    mutex = True
    for keyA, valueA in A.items():
        for keyB, valueB in B.items():
            if keyA != keyB and mutex:
                continue
            if keyA == keyB:
                mutex = False
            else:
                if keyA in valueB:
                    valueB.remove(keyA)
        mutex = True
    return countArrows(B)
        
        
        
def arrowsToEdges(A):
    """
    arrowsToEdges - wandelt einen gerichteten Graphen in einen Ungerichteten
    Dabei werden die Nachbarknoten eines Key-Knotens durchgegangen.
    Wenn dieser Nachbarknoten dann als Key irgendwo auftaucht
    wird er zu den Nachbarknoten dieses Keys hinzugefügt.
    """
    B = A.copy()
    for keyA, valueA in A.items():
        for node in valueA:
            for keyB, valueB in B.items():
                if keyA in valueB:
                    continue
                if keyB == node:
                    valueB.extend(keyA)
    return B

def beautyPrint(A):
    """
    beautyPrint - Gibt den Graph in einem hübschen Format aus
    """
    print("""Node | connected Neighbours\n---------------------------""")
    for key, value in A.items():
        print(key,": ",value,)
    print("---------------------------")

beautyPrint(G)
#print(countArrows(G))
beautyPrint(arrowsToEdges(G))
countEdges(arrowsToEdges(G))
#beautyPrint(T)
#beautyPrint(arrowsToEdges(T))
