def main():
    t = int(input())
    for _ in range(t):
        w = int(input())
        p = int(input())
        arr = list(map(int , input().split()))
        dp = [False]*(w+1)
        dp[0] = True
        for i in arr:
            for j in range(w , i-1 , -1):
                if dp[j]:continue
                dp[j] = dp[j-i]
        if dp[w]:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
