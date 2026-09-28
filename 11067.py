def main():
    while True:
        w , h = map(int , input().split())
        if w == 0 and h == 0:break
        n = int(input())
        wolves = set()
        for i in range(n):
            x , y = map(int , input().split())
            wolves.add((x , y))
        dp = [[0]*(h+1) for _ in range(w+1)]
        if (0 , 0) not in wolves:
            dp[0][0] = 1
        for i in range(1 , w+1):
            if (i , 0) in wolves:continue
            dp[i][0] = dp[i-1][0]
        for i in range(1 , h+1):
            if (0 , i) in wolves:continue
            dp[0][i] = dp[0][i-1]
        for i in range(1 , w+1):
            for j in range(1 , h+1):
                if (i , j) in wolves:continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        ans = dp[w][h]
        if ans == 0:
            print("There is no path.")
        elif ans == 1:
            print("There is one path from Little Red Riding Hood's house to her grandmother's house.")
        else:
            print(f"There are {ans} paths from Little Red Riding Hood's house to her grandmother's house.")

if __name__ == "__main__":
    main()
