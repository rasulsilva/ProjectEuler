"""
rasul silva
Project Euler 
problem 10
"""
def is_prime(num):
    if num == 0 or num == 1: return False
    if num % 2 == 0: return False
    for value in range(2,int(num**.5) + 1):
        if num % value == 0:
            return False
    return True

def generate_prime_list(range_top):
    primes = [2]
    for i in range(2,range_top+1):
        if (is_prime(i)):
            primes.append(i)
    return primes    

def sum_up_list(input_list):
    list_sum = 0
    for item in input_list:
        list_sum = list_sum + item
    return list_sum
if __name__ == "__main__":
    print(sum_up_list(generate_prime_list(1999999)))  
    # answer is 142913828922