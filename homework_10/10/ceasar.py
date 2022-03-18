russian_alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
                    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
leng = len(russian_alphabet)
step = int(input("Enter the step of encryption:\n"))
phrase = input("Enter you message:\n")

phrase = list(phrase)
encrypted_phrase = []

for i in range(len(phrase)):
    symbol = phrase[i]
    if symbol in russian_alphabet:
        letter = russian_alphabet.index(symbol)
        if letter + step < leng:
            symbol = russian_alphabet[letter + step]
        else:
            symbol = russian_alphabet[letter + step - leng]
        encrypted_phrase.append(symbol)
    else:
        encrypted_phrase.append(phrase[i])

print(''.join(encrypted_phrase))
