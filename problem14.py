"""
rasul silva
Project Euler 
problem 14
"""

#calculates collatz sequence length for each number in range
def Collatzcalculation(rangestart, rangeend):
    sequencelength = []#the number of calculations it takes to reach 1
    ivalues = [] #list of starting values
    for i in range (rangestart,rangeend+1):
        ivalues.append(i)#add starting values to list
        #print("calculate sequence for: " + str(i))
        sequence = []#into this will append the result of each calculation
        m = i #i copy
        j=1 # incrementer
        sequence.append(m)
        while m != 1:
            if m%2 == 0:#even procedure
                m = m/2
                sequence.append(m)
                j += 1
            else:#odd procedure
                m = 3*m + 1
                sequence.append(m)
                j += 1
                
        #print(sequence)
        sequencelength.append(j)
        #print("sequence length is " + str(j) + " for a starting value of " + str(i) + "\n")
    
    return sequencelength, ivalues

if __name__ == '__main__':
    
    sequencelength, ivalues = Collatzcalculation(1,999999)
    print( "maximum sequence length: {}".format( max(sequencelength)))
    '''
    answer is length 525, this can be optimized by storing previous 
    collatz sequence lengths. For instance, if in the collatz sequence of 
    one number we encounter a number we've already seen then we know the answer
    from that point on. the only drawback is we use memory to store these lengths.
    I'll come back to this one
    '''
    

