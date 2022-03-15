friends = int(input("Amount of friends:\n"))
money_of_friends = [0 for _ in range(friends)]

debentures = int(input("Amount of debentures:\n"))

for i in range(debentures):
    print("№", i + 1)
    recipient = int(input("Recipient: "))
    sender = int(input("Sender: "))
    summa = int(input("Summa: "))
    money_of_friends[recipient - 1] -= summa
    money_of_friends[sender - 1] += summa

print("Friends' balances: ")
for i in range(friends):
    print(i + 1, money_of_friends[i])
