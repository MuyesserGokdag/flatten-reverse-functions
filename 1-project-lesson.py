# Soru 1
"""
1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) 
oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

Örnek olarak:

    input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

    output: [1,'a','cat',2,3,'dog',4,5]
"""

liste = [[1, "a", ["cat"], 2], [[[3]], "dog"], 4, 5]

def flatten(liste):
    result = []

    for element in liste:
        if type(element) == list:
            result.extend(flatten(element))
        else:
            result.append(element)
    return result

cıktı = flatten(liste)
print(cıktı) 
