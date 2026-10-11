from math import *

def dis(a , b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def check(a , buf):
    
    for b in buf:
        if dis(a , b) <= a[2]+b[2]:
            return False
    return True

def cal(temp):
    count = 0
    for t in temp:
        count += t[2]**2
    return count

def solve(n , ps):
    
    ans = 0
    def dfs(now , buf):
        nonlocal ans
        if now >= n:
            ans = max(ans , cal(buf))
            return 
        if check(ps[now] , buf):
            dfs(now+1 , buf+[ps[now]])
        dfs(now+1 , buf)

    dfs(0 , [])
    return ans

def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        ps = []
        for i in range(n):
            ps.append(list(map(int , input().split())))
        ans = solve(n , ps)
        print(ans)

if __name__ == "__main__":
    main()
