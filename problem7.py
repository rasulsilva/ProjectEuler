"""
rasul silva
Project Euler 
problem 7
"""
import time
import math

def isprime(num):#return 1 for prime, 0 for not prime
    if (num % 2 == 0):#if even don't waste your time
        return 0
    for i in range (3,int(math.sqrt(num))+1,2):#only check up to sqrt and and skip evens
        if (num % i == 0):
            return 0
    return 1


if __name__ == "__main__":
    inc = 0
    primecount = 0
    
    before = time.time()
    while (primecount < 10001):
        if (isprime(inc) == 1):
            #print(inc)
            primecount = primecount + 1
        inc = inc + 1
    after = time.time()
    
    print("inc: ",inc-1)
    print("time:", after - before)
    