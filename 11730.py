from collections import deque
from math import *

def generate(limit):
    
    seive = [True]*limit
    seive[0] = seive[1] = False
    for i in range(2 , int(sqrt(limit)) + 1):
        if seive[i]:
            for j in range(i*i , limit , i):
                seive[j] = False
    primes = []
    for k , v in enumerate(seive):
        if v:
            primes.append(k)
    return seive , primes

seive , primes = generate(1100)
def bfs(a , b):
    global seive , primes
    if a == b:return 0
    
    q = deque([[a , 0]])
    check = set()
    check.add(a)

    while q:
        now , count = q.popleft()

        if seive[now]:continue
        for i in primes:
            if now % i == 0:
                x = now+i
                if x in check:continue
                if x == b:
                    return count + 1
                if x < b:
                    q.append([x , count + 1])
                    check.add(x)
    return -1

def main():
    now = 0
    while True:
        a , b = map(int , input().split())
        if a == 0 and b == 0:break
        ans = bfs(a , b)
        print(f"Case {now+1}: {ans}")
        now += 1

if __name__ == "__main__":
    main()
