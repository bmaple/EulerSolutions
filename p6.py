#!/usr/bin/python
def sq(x):
    return x*x
def sumSq(ceiling):
    sumOfsq = 0
    for num in range(1, ceiling+1):
        sumOfsq += sq(num)
    return sumOfsq

def sqSum(ceiling):
    sqOfSum = 0
    for num in range(1, ceiling+1):
        sqOfSum += num
    return sq(sqOfSum)

def main():
   print -(sumSq(100) - sqSum(100))
if __name__ == '__main__':
    main()
