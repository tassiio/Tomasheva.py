from magic_cl import *
w = Water()
a = Air()

smth = w + w
if smth is None:
    print("I don't know such reactions :(")
else:
    print(smth.answer)
