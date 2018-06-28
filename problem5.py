"""
rasul silva
Project Euler 
problem 5
"""
#answer:  232792560
#runtime: 3.0369048 seconds

import time

factlist = [11,12,13,14,15,16,17,18,19,20]
'''
all numbers below 11 have multiples that
exist in the range (11 to 20), so we don't
need to include them
'''
def isdivbylist(num, factlist):
    for i in factlist:
        if (num % i != 0):
            return 0
    return 1
    

if __name__ == '__main__':

    flag = 0
    inc = 20
    before = time.time()
    while (flag == 0):
        if (isdivbylist(inc,factlist) == 1):
           answer = inc
           flag = 1
        inc = inc + 20
    after = time.time()
    
    print (answer)
    print(after - before)
    

    