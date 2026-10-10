from math import *

def main():
    now = 1
    while True:
        n = int(input())
        if n == 0:break
        ans = 0
        for a in range(1 , ceil(n/3)):
            ans += (ceil((n - a)/2) - a - 1)
        print(f"Case {now}: {ans}")
        now += 1

if __name__ == "__main__":
    main()
