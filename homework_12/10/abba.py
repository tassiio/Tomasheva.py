string = input("Enter any string:\n")
string = string.lower()

frequency_of_letters = {}
for letter in string:
    if frequency_of_letters.get(letter) is None:
        frequency_of_letters[letter] = 1
    else:
        frequency_of_letters[letter] += 1

counter = 0

for letter in frequency_of_letters.keys():
    if frequency_of_letters[letter] % 2 != 0:
        counter += 1
if counter > 1:
    print("It's not a mixed palindrome.")
else:
    print("It is a mixed palindrome.")
