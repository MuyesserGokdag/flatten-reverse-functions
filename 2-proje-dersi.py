# Soru 2
"""
2- Verilen listenin içindeki elemanları tersine döndüren 
bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste 
içeriyorsa onların elemanlarını da tersine döndürün. 

Örnek olarak:

    input: [[1, 2], [3, 4], [5, 6, 7]]

    output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

l = [[1, 2], [3, 4], [5, 6, 7]]

def tersine(l):
    
    result = []
    
    for eleman in l[::-1]:
        if type(eleman) == list:
            result.append(tersine(eleman))
        else:
            result.append(eleman)
    return result

cıktı = tersine(l)
print(cıktı) 