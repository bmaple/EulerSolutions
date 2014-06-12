#!/usr/bin/python
import math
def sq(x): 
    return x * x

def siv(num):
    nums = [True] * int(math.sqrt(num))  
    for i in range (2, int(math.sqrt(num))): 
        if nums[i] == True:
            for s in range(sq(i), int(math.sqrt(num)), i): #issue is here need to make it increment by i
                nums[s] = False
    return nums 

def biggestPrime(num):
    primes = siv(num)
    largestIndex = 0
    for index, i in enumerate(primes, start = 1):
        '''if i == True and index > largestIndex and num % index == 0:
            largestIndex = index
    return largestIndex'''
        if i == True and num % index == 0:
            print(index)

def main():
    lP = 600851475143
    #print(biggestPrime(lP))
    biggestPrime(lP)
if __name__ == '__main__':
    main()
