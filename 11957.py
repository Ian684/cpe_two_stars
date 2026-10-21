def main():
    test = int(input())
    for case in range(test):
        n = int(input())
        arr = []
        for i in range(n):
            arr.append(input())

        dp = [[0]*n for _ in range(n)]
        for i in range(n-1 , -1 , -1):
            for j in range(n):
                if arr[i][j] == 'W':
                    dp[i][j] = 1
                    continue
                if arr[i][j] == '.':
                    if i+1 < n and j-1 >= 0 and arr[i+1][j-1] == 'B':
                        if i+2 < n and j-2 >= 0:
                            dp[i][j] += dp[i+2][j-2]
                    elif i+1 < n and j-1 >= 0:
                        dp[i][j] += dp[i+1][j-1]
                    if i+1 < n and j+1 < n and arr[i+1][j+1] == 'B':
                        if i+2 < n and j+2 < n:
                            dp[i][j] += dp[i+2][j+2]
                    elif i+1 < n and j+1 < n:
                        dp[i][j] += dp[i+1][j+1]
                    dp[i][j] %= 1000007

        ans = 0
        for i in range(n):
            ans += dp[0][i]
            ans %= 1000007
        print(f"Case {case+1}: {ans}")

if __name__ == "__main__":
    main()
