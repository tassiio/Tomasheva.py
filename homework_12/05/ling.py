text = input()
frequency_orig = {letter: text.count(letter) for letter in set(text)}
print(frequency_orig)
keys_new = frequency_orig.values()
# print(frequency_orig.keys())

inverse_dict = {key_new: [] for key_new in keys_new}
print(inverse_dict)
for i in inverse_dict.keys():
    for key in frequency_orig.keys():
        if frequency_orig[key] == i:
            inverse_dict[i].append(key)
print(inverse_dict)
