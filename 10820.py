from math import *

def generate(limit):

    slimit = int(sqrt(limit)) + 1
    seive = [True]*slimit
    seive[0] = seive[1] = False
    for i in range(2 , int(sqrt(slimit)) + 1):
        if seive[i]:
            for j in range(i*i , slimit , i):
                seive[j] = False

    prime = []
    for k , v in enumerate(seive):
        if v:
            prime.append(k)

    f = [0 , 1]
    for i in range(2 , limit):
        phi = i
        temp = i
        for p in prime:
            if temp % p == 0:
                phi *= (1 - (1/p))
                while temp % p == 0:
                    temp //= p
        if temp != 1:
            phi *= (1 - (1/temp))
                
        f.append(f[i-1]+phi)

    return f

def main():
    f = generate(50001)
    while True:
        n = int(input())
        if n == 0:break
        print(int(f[n]*2-1))

if __name__ == "__main__":
    main()
