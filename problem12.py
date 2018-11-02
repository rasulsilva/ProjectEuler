"""
rasul silva
Project Euler 
problem 12

I will revisit this problem, this solution is too slow
"""


def generate_divisor_list(num):
    div_list = []
    for i in range(1, int(num**.5)+1):
        if num % i == 0:
            div_list.append(i)      
            div_list.append(num/i)  
    return len(div_list)

def find_first_multi_divisor(num_of_divisors = 6):
    tri_num = 1
    tri_list = [tri_num]
    while(True):
        tri_num = sum(tri_list)
        if generate_divisor_list(tri_num) == num_of_divisors:
            return tri_num
        tri_list.append(tri_list[-1]+1)

if __name__ == "__main__":
    #print(generate_divisor_list(28))
    print(find_first_multi_divisor(num_of_divisors = 500))
