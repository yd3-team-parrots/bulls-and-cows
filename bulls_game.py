'''
1. take input
2. input to list
3. use random 
4. take list length of 4
'''

import random
rl = list(random.sample(range(10), 4))
bull = 0
cow = 0
##print(rl)
##print(il)

while bull != 4:
    il = list(input("Please type the stream of 4 numbers separated by white space: ").split(' '))
    for i in range(len(rl)):
        if str(rl[i]) in il:
            cow += 1
        else:
            pass 
        for j in range(len(il)):
            if rl[i] == il[j] and i==j:
                bull += 1
            else:
                pass
    print(bull, cow)  
