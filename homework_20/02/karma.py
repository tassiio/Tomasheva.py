from karma_cl import *
life = Life()
krm = open('karma_errors.log', 'w+')
krm.close()
while life.your_karma < life.karma_max:
    print(life.your_karma)
    life.one_day()
