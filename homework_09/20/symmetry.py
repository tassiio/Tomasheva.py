amount = int(input("Enter amount of numbers:\n"))
palindrome = [int(input("Enter number:\n")) for i in range(amount)]

print(palindrome)
adding = 0
while palindrome != palindrome[::-1]:
    palindrome.insert(amount, palindrome[adding])
    adding += 1

print("The sequence:", palindrome)
print("You need to add", adding, "numbers.")

for i in range(amount, len(palindrome)):
    print(palindrome[i], end=' ')
