#!/usr/bin/python
import sys
def f(x, val, prev):
    if x == 0:
        return prev
    if x == 1:
        return val 
    else: 
        return f(x-1, val+prev, val)

def main():
    i = 0; 
    totalNum = 0
    curNum = f(i, 1, 0)
    if curNum % 2 == 0:
        totalNum += curNum
    i += 1
    while curNum < 4000000:
        curNum = f(i, 1, 0)
        if curNum % 2 == 0:
            totalNum += curNum
        i += 1
    print(totalNum)

if __name__=="__main__":
    main()
