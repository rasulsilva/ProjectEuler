"""
rasul silva
Project Euler
problem 2
"""


addend1,addend2,addend3 = 1,2,0
fibsum = 0

while ((addend1 + addend2) < 4000000):
    addend3 = addend1 + addend2
    if addend3 % 2 == 0:
        fibsum += addend3
    addend1 = addend2
    addend2 = addend3
    
fibsum += 2 #this is because the 2 does not get included

print(fibsum)
        
          
    