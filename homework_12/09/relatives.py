amount_people = int(input("Enter amount of people: \n"))
# pairs = []
pairs_dict = {}
for i in range(amount_people - 1):
    # pairs.append(list(input(f'{i + 1} pair: ').split(" ")))
    child, parent = input(f'{i+1} pair: ').split(" ")
    pairs_dict[child] = parent
# print(pairs)
# print(pairs_dict)

tree_dict = {}
for people in pairs_dict.values():
    if people not in pairs_dict.keys():
        tree_dict[people] = 0
for person in pairs_dict.keys():
    tree_dict[person] = tree_dict[pairs_dict[person]] + 1

print("Level of every family member:")
for key in sorted(tree_dict):
    print("%14s%3d" % (key, tree_dict[key]))
