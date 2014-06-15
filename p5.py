#!/usr/bin/python
def smMul():
    ceiling = 900000000
    for number in range(20, ceiling, 20):
        divisible = True 
        for divisor in range(2, 21):
            if number % divisor != 0:
                divisible = False
        if divisible: 
            return number
        divisible = True
def main():
   print smMul()
if __name__ == '__main__':
    main()
