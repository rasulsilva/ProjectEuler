"""
rasul silva
Project Euler 
problem 6
"""

def sumofsquares(start,finish):
    sum = 0;
    for i in range(start,finish+1):
        sum += i*i
    return sum

def squareofsum(start,finish):
    sum = 0;
    for i in range(start,finish+1):
        sum += i
    return sum*sum

        
if __name__ == "__main__":
    answer = squareofsum(1,100) - sumofsquares(1,100)
    print(answer)