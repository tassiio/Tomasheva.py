from my_dict_cl import MyDict

mydict = MyDict()
for i in range(1, 6):
    mydict[i] = f'{i}{i}'
print(mydict)
print(mydict.get('d'))
