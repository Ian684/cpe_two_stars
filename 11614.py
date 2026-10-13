from math import *

def main():
    test = int(input())
    a = b = 1
    for _ in range(test):
        c = -2*int(input())
        print(int((-b + sqrt(b**2 - 4*a*c))/(2*a)))

if __name__ == "__main__":
    main()
