vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
text = input("Enter the text: ")
text = list(text)
vowels = [text[i] for i in range(len(text)) if text[i] in vowels_list]
print("The list of vowels: ", vowels)
print("Amount: ", len(vowels))
