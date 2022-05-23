from family_cl import Parent
from family_cl import Child


child_1 = Child('Child_1', 5, 'Good', 'hungry')
child_2 = Child('Child_2', 7, 'Sad', 'Wel-fed')
parent = Parent('Parent', 30, [child_1.name_ch, child_2.name_ch])

parent.calm(child_2)
# parent.check(child_1)
print(child_2)
parent.feed(child_1)
print(child_1)
