pairs = int(input("Enter amount of pairs of synonymes:\n"))
dict_of_syns = {}
for i in range(pairs):
    key, syn = input().split()
    dict_of_syns[key] = syn
    dict_of_syns[syn] = key
word = input("Enter the word:\n")
No_Word = True
for key in dict_of_syns:
    if dict_of_syns[key].lower() == word.lower():
        print("The synonym for your word:", key)
        No_Word = False
if No_Word:
    print("There is no such words in the dictionary.")
