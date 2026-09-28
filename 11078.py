def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        for i in range(n):
            arr.append(int(input()))
        arr = arr[::-1]
        dp = [0]*n
        dp[0] = - 1 << 32
        for i in range(1 , n):
            dp[i] = max(arr[i]-arr[i-1] , arr[i]-arr[i-1]+dp[i-1])
        print(max(dp))

if __name__ == "__main__":
    main()
