from math import *

def main():
    test = int(input())
    for _ in range(test):
        n , a , b = map(int , input().split())
        total = (1 << n) - 1
        small = ((1 << (n - max(int(log(a , 2)) , int(log(b , 2))))) - 1)
        total -= small
        total += 1
        print(total)

if __name__ == "__main__":
    main()
