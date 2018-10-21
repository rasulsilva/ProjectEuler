"""
rasul silva
Project Euler 
problem 3
"""
import math

#check if num is prime: return True or False
def is_prime(num):
    if num == 0 or num == 1: return False
    if num % 2 == 0: return False
    for value in range(2,int(num**.5) + 1):
        if num % value == 0:
            return False
    return True

#generate list of prime numbers up to range_top
def generate_prime_list(range_top):
    primes = [2]
    for i in range(2,range_top+1):
        if (is_prime(i)):
            primes.append(i)
    return primes 

if __name__ == "__main__":
    number = 600851475143
    sqrt = int(number ** .5)
    print("number:{}".format(number))
    print("sqrt  :{}".format(sqrt))
    prime_list = generate_prime_list(sqrt + 1)
    biggest_factor = 1
    for prime in prime_list:
        if number % prime == 0:
            biggest_factor = prime
    print("biggest prime factor: {}".format(biggest_factor))

