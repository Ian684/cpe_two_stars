def solve(n , remain):
    
    dp = [[0]*(remain+1) for _ in range(n)]
    for j in range(remain+1):
        dp[0][j] = 1

    for i in range(1 , n):
        for j in range(remain+1):
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]

    return dp[n-1][remain]

def main():
    t = int(input())
    for _ in range(t):
        n , t , p = map(int , input().split())
        remain = t - p*n
        if remain < 0:
            print(0)
            continue
        elif remain == 0:
            print(1)
            continue
        ans = solve(n , remain)
        print(ans)

if __name__ == "__main__":
    main()
