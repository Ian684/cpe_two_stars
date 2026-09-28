from math import *

def generate(limit):

    prime = [False]*limit
    for i in range(2 , int(sqrt(limit))+1):
        if not prime[i]:
            for j in range(i*i , limit , i):
                prime[j] = True

    for i in range(4 , limit):
        if prime[i]:
            for j in range(i*2 , limit , i):
                prime[j] = False

    return prime

def main():
    
    com_prime = generate(2**20+100)

    while True:
        try:
            n = int(input())
            arr = []
            while n > 0:
                line = list(map(int , input().split()))
                arr += line
                n -= len(line)
        except EOFError:break
        count = 0
        for a in arr:
            if com_prime[a]:
                count += 1
        print(count)

if __name__ == "__main__":
    main()
