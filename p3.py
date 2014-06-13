#!/usr/bin/python
import math
def sq(x): 
    return x * x

def siv(num):
    nums = [True] * int(math.sqrt(num))  
    for i in range (2, int(math.sqrt(num))): 
        if nums[i] == True:
            for s in range(sq(i), int(math.sqrt(num)), i): 
                nums[s] = False
    return nums 

def biggestPrime(num):
    primes = siv(num)
    for index, val in reversed(list(enumerate(primes))):
        if val and num % index == 0: return index

def main():
    lP = 600851475143
    print(biggestPrime(lP))
if __name__ == '__main__':
    main()
