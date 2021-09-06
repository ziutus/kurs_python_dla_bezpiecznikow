import json
import urllib.request

"""Znajdź otwarte API czegoś, co cię interesuje np. sportu lub strony z ocenami filmów.

Możesz znaleźć takie API tutaj: https://github.com/public-apis/public-apis.
Stwórz skrypt, który pobiera z tego API interesujące Cię dane i przetwarza je w jakiś sposób.
Skrypt musi wykonywać przynajmniej dwa zapytania do API i zawierać minimum jedną pętlę lub instrukcję if.
Przykład: najczęściej wygrywający kierowca formuły 1 w ciągu ostatnich dwóch sezonów.
"""

"""Poniższy kod znajduje w obu tabelach NBP informacje o średnim kursie walut zdefiniowanych w liście currencyToFind """

currencyToFind = ["USD", "EUR", "GEL"]
tableADate = ''
tableBDate = ''
currences = {}

# Table A
link = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
with urllib.request.urlopen(link) as response:
    html = response.read().decode('utf-8')

jdata = json.loads(html)

currences["DATE"] = jdata[0]['effectiveDate'].replace('-', '.')
for currency in jdata[0]['rates']:
    if currency['code'] in currencyToFind:
        currences[currency['code']] = currency['mid']

# Table B
link = "http://api.nbp.pl/api/exchangerates/tables/B/?format=json"
with urllib.request.urlopen(link) as response:
    html2 = response.read().decode('utf-8')

jdata2 = json.loads(html2)

tableBDate = jdata2[0]['effectiveDate']
for currency in jdata2[0]['rates']:
    if currency['code'] in currencyToFind:
        currences[currency['code']] = currency['mid']

print(json.dumps(currences))
