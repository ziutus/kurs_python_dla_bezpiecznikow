"""
Stwórz skrypt, który:
1. Tworzy listę liczb od 0 do 9 (pętla for)
2. Iteruje po tej liście pętlą for lub while i wypisuje jej zawartość
3. Usuwa liczby 3 i 5 z listy [ list.remove() ]
3. Zamienia liczby 8 i 9 na stringi (list.remove() lub list.pop() i list.append(), bądź zwykłe przypisanie list[8] = ‘8’
Lista po tych przekształceniach powinna wyglądać tak: [0, 1, 2, 4, 6, 7, ‘8’, ‘9’]
"""

list = [ i for i in range(0,10) ]

print("Utworzona lista to:", list)

print("Wartości w liście to: ", end = '')
for i in list:
    print( f"{i} ", end = '')
print("")
list.remove(3)
list.remove(5)
print("Lista po usunięciu wartości 3 i 5:", list)

list[6]="8"
list[7]="9"
print("Lista po zamianie liczb 8 i 9 na stringi:", list)
