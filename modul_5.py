import argparse
import json
import secrets
from hashlib import sha256
from base64 import b64decode, b64encode, encode
from pyperclip import copy


# Stworz skrypt, ktory:
# 1. Pobiera od uzytkownika 1 argument wymagany i 1 opcjonalny (argparse)
# 2. Tworzy slownik z tych danych oraz bezpiecznego sekretu, a nastepnie zamienia go na stringa (secrets, json)
# 3. Tworzy skrot SHA256 danych (hashlib)
# 4. Koduje calosc base64
# 5. Kopiuje zawartosc do schowka (pyperclip)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Moja odpowiedz do zdania z modulu 5')
    parser.add_argument('-m', '--mandatory', type=str, required=True, help='Argument wymagany')
    parser.add_argument('-o', '--optional', default=None, help='Argument opcjonalny')
    args = parser.parse_args()
    print(args)

    moj_slownik = {
        'mandatory': args.mandatory,
        'optional': args.optional,
        'bezpieczny_sekret': secrets.token_urlsafe()
    }

    moj_slownik_string = json.dumps(moj_slownik)
    skrot = sha256(moj_slownik_string.encode('utf8')).hexdigest()

    data = f"'data': {moj_slownik_string},'skrot': {skrot}"

    print(moj_slownik)
    print(moj_slownik_string)
    print(data)
    data_base64 = b64encode(data.encode()).decode()
    print(data_base64)
    copy(data_base64)
    print("Data znajdują się już w schowku systemowym. Wystarczy teraz wkleic dane")
