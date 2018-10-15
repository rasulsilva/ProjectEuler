"""
rasul silva
Project Euler 
problem 6
"""
import math

def is_pthag_triplet(a,b,c):
    if ((a**2 + b**2) == c**2):
        return True
    return False

def find_triplet(top_sum = 1000):
    for a in range (1,math.ceil(top_sum/3)):
        for b in range (1,math.ceil(top_sum/2)):
            c = 1000 - a - b
            if (is_pthag_triplet(a,b,c)):
                return a,b,c

if __name__ == "__main__":
    try:
        a,b,c = find_triplet()
    except:
        "no triplet found"
        
    print("the pythagorean triplet is ({},{},{})".format(a,b,c))
    print("then the product is {}".format(a*b*c))

    '''
    explanation of ranges:
    A+B+C = SUM, A must be less than sum/3, because if it were larger then
    there wouldn't be enough left for A+B+C to still sum to SUM without
    breaking the rule a<b<c. We can deduce the same for b by looking at
    the worst case. 
    For this example let's test the boundary condition
    example:
        A = 1000/3 = 333.333, 
        B>A, so B  = 334
        C>B, so C  = 335
        A+B+C = 333+334+335 = 1002 > 1000, hopefully this demonstrates the idea
        A has to be less than 1000/3
    '''