# don't blame me if the code is not working

import random

random_num =[]

for i in range(10):
    num = random.randrange(1, 10)
    if num not in random_num:
        random_num.append(num)
    else: 
        print(random_num)

       
