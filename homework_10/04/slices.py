alphabet = 'abcdefg'

alphabet = list(alphabet)

print("1:", ''.join(([alphabet[i] for i in range(len(alphabet))])))
print("2:", ''.join(alphabet[::-1]))
print("3:", ''.join(alphabet[::2]))
print("4:", ''.join(alphabet[1::2]))
print("5:", ''.join(alphabet[:1]))
print("6:", ''.join(alphabet[:-2:-1]))
print("7:", ''.join(alphabet[3:4]))
print("8:", ''.join(alphabet[-3::]))
print("9:", ''.join(alphabet[3:5]))
print("10:", ''.join(alphabet[-3:-5:-1]))
