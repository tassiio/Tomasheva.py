amount = int(input("How many containers are there?\n"))

containers = []
# input processing
for i in range(amount):
    print("№", i + 1, ":", end=' ')
    check = int(input())
    if i == 0:
        while check > 200:
            print("№", i + 1, "-> repeat :", end=' ')
            check = int(input())
    else:
        while check > 200 or check > containers[i-1]:
            print("№", i + 1, " -> repeat :", end=' ')
            check = int(input())
    containers.append(check)
#

new_one = int(input("Enter the mass of the new one:\n"))
while new_one > 200:
    print("Repeat (< 200):", end=' ')
    new_one = int(input())

number = 0
k = 0
cont = 0
while containers[k] >= new_one:
    cont = containers[k]
    k += 1
    number = k

# add = containers.count(cont)
print("Number of the new one is:", number + 1)
