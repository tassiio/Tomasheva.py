from company_cl import *

# for i in range(9):
#    if i < 3:

#    company.append()

company = [Manager('bob', 'dilan', 33), Agent('lucy', 'n', 25, 500), Worker('Tom', 'Tom', 18, 400)]
for person in company:
    print(person.salary())
