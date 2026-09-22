def main():
    now = 1
    while True:
        try:
            line = list(map(int , input().split()))
        except EOFError:break
        n = line[0]
        arr = line[1:]
        if arr != sorted(arr):
            print(f"Case #{now}: {' '.join(map(str , arr))}")
            print("This is not an A-sequence.")
            now += 1
            continue
        flag = True
        if arr[0] < 1:
            flag = False
        for i in range(1 , n):
            a = arr[i]
            if a <= arr[i-1] or a < 1:
                flag = False
                break
        if not flag:
            print(f"Case #{now}: {' '.join(map(str , arr))}")
            print("This is not an A-sequence.")
            now += 1
            continue
        
        dp = [0]*1001
        dp[0] = 1
        for i in arr:
            for j in range(1000 , i-1 , -1):
                dp[j] += dp[j-i]
        flag = True
        for a in arr:
            if dp[a] > 1:
                flag = False
                break
        print(f"Case #{now}: {' '.join(map(str , arr))}")
        now += 1
        if flag:
            print("This is an A-sequence.")
        else:
            print("This is not an A-sequence.")

if __name__ == "__main__":
    main()
