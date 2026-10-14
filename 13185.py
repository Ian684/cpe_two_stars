from math import *

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        c = 0
        for i in range(1 , int(sqrt(n))+1):
            if n % i == 0:
                c += i + n//i
        if int(sqrt(n))**2 == n:
            c -= int(sqrt(n))
        c -= n
        if n == c:
            print("perfect")
        elif n > c:
            print("deficient")
        elif n < c:
            print("abundant")

if __name__ == "__main__":
    main()
