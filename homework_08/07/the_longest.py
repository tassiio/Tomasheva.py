import string

tab = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
text = input("Enter any text:\n")
f_text = text.translate(tab).split()
# print(f_text)

print(max(f_text, key=len))
