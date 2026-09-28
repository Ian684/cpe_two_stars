def main():
    c = [1 , 1]
    for i in range(2 , 13):
        c.append(c[i-1]*i)

    while True:
        n = int(input())
        if n == 0:break
        arr = list(map(int , input().split()))
        nums = [0]*13
        p = c[n]
        for a in arr:
            nums[a] += 1
        for i in nums:
            p //= c[i]
        p = int(p / len(arr) * sum(arr))
        ans = 0
        for i in range(n):
            ans += p * 10**i
        print(ans)

if __name__ == "__main__":
    main()
