# Kurs "Python dla bezpieczników"

Prace domowe dla kursu: ["Python dla bezpieczników"](https://szkolasecurity.pl/python-dla-bezpiecznikow/).

## Zadanie po module 1
Stwórz skrypt, który:
1. Tworzy listę liczb od 0 do 9 (pętla for)
2. Iteruje po tej liście pętlą for lub while i wypisuje jej zawartość
3. Usuwa liczby 3 i 5 z listy [ list.remove() ]
3. Zamienia liczby 8 i 9 na stringi (list.remove() lub list.pop() i list.append(), bądź zwykłe przypisanie list[8] = ‘8’
Lista po tych przekształceniach powinna wyglądać tak: [0, 1, 2, 4, 6, 7, ‘8’, ‘9’]

## Zadanie po module 2
Napisz skrypt, przefiltruje plik ffuf.out i zostawi jedynie ściezki z rozszerzeniem .php, w których nazwie pliku (nie folderu) znajduje się słowo “admin” lub “user”

## Zadanie po module 3
Znajdź otwarte API czegoś, co cię interesuje np. sportu lub strony z ocenami filmów.

Możesz znaleźć takie API tutaj: https://github.com/public-apis/public-apis.
Stwórz skrypt, który pobiera z tego API interesujące Cię dane i przetwarza je w jakiś sposób.
Skrypt musi wykonywać przynajmniej dwa zapytania do API i zawierać minimum jedną pętlę lub instrukcję if.
Przykład: najczęściej wygrywający kierowca formuły 1 w ciągu ostatnich dwóch sezonów.

## Zadanie po module 5

Stwórz skrypt, który:
1. Pobiera od użytkownika 1 argument wymagany i 1 opcjonalny (argparse)
2. Tworzy słownik z tych danych oraz bezpiecznego sekretu, a następnie zamienia go na stringa (secrets, json)
3. Tworzy skrót SHA256 danych (hashlib)
4. Koduje całość base64
5. Kopiuje zawartość do schowka (pyperclip)
