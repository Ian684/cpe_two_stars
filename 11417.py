from math import *

def main():
    while True:
        n = int(input())
        if n == 0:break
        g = 0
        for i in range(1 , n):
            for j in range(i+1 , n+1):
                g += gcd(i , j)

        print(g)

if __name__ == "__main__":
    main()
