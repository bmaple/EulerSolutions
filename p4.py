#!/usr/bin/python
def sq(x):
    return x*x
def palidromes(minNum, maxNum):
    largestProduct = sq(minNum)
    smallestProduct = sq(maxNum)
    for number in range(999, 100, -1):
        palindron = int(str(number) + str(number)[::-1])
        for i in range(100, 999): 
            if 100 <= palindron / i <= 999 and i * (palindron/i) == palindron: 
                print i, palindron / i 
                return palindron
def main():
   print palidromes(100, 999)
if __name__ == '__main__':
    main()
