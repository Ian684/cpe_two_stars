from math import *

def solve(n):

    ans = set()
    def dfs(aim , fac):
        nonlocal ans
        if aim <= 1:
            return 
        for i in range(2 , int(sqrt(aim))+1):
            if aim % i == 0:
                fac.append(i)
                ans.add(tuple(sorted(fac+[aim//i])))
                dfs(aim//i , fac)
                fac.pop()

    dfs(n , [])
    return ans

def main():
    while True:
        n = int(input())
        if n == 0:break
        ans = solve(n)
        print(len(ans))
        for i in sorted(ans):
            print(" ".join(map(str , i)))

if __name__ == "__main__":
    main()
