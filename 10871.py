from math import *

def generate(limit):
    
    seive = [True]*limit
    seive[0] = seive[1] = False
    for i in range(2 , int(sqrt(limit)) + 1):
        if seive[i]:
            for j in range(i*i , limit , i):
                seive[j] = False

    prime = set()
    for k , v in enumerate(seive):
        if v:
            prime.add(k)
    
    return prime

def main():
    prime = generate(200000)
    t = int(input())
    for _ in range(t):
        line = list(map(int , input().split()))
        n = line[0]
        arr = line[1:]
        prefix = arr[::]
        for i in range(1 , n):
            prefix[i] += prefix[i-1]
        ans = None
        for l in range(1 , n):
            for i in range(n-l):
                j = i + l
                if i - 1 >= 0 and prefix[j] - prefix[i-1] in prime:
                    ans = [j+1-i] + arr[i:j+1]
                    break
                if i - 1 < 0 and prefix[j] in prime:
                    ans = [j+1-i] + arr[i:j+1]
                    break
            if ans is not None:
                break
        if ans is None:
            print("This sequence is anti-primed.")
        else:
            print(f"Shortest primed subsequence is length {ans[0]}: {' '.join(map(str , ans[1:]))}")

if __name__ == "__main__":
    main()
