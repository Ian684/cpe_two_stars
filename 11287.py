from math import *

def generate(limit):

    limit = int(sqrt(limit)) + 1
    seive = [True]*limit
    seive[0] = seive[1] = False
    for i in range(2 , int(sqrt(limit)) + 1):
        if seive[i]:
            for j in range(i*i , limit , i):
                seive[j] = False

    prime = []
    for k , v in enumerate(seive):
        if v:
            prime.append(k)

    return prime

def main():

    prime = generate(10**9+100)
    while True:
        p , a = map(int , input().split())
        if p == 0 and a == 0:break
        count = 0
        temp = p
        for pp in prime:
            while temp % pp == 0:
                temp //= pp
                count += 1
                if count > 1:break
            if count > 1:
                break
        if not (count > 1 or (count == 1 and temp != 1)):
            print("no")
            continue

        aim = a
        odd = 1
        temp = p
        while True:
            if temp <= 1:break
            if temp & 1:
                odd = (odd * aim) % p
                temp -= 1
            aim = (aim * aim) % p
            temp //= 2
            
        if (aim * odd) % p == a:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    main()
