def main():
    now = 1
    while True:
        n = int(input())
        if n == 0:break
        arr = []
        for i in range(n):
            arr.append(list(map(int , input().split()[::-1])))
        ans , s = 0 , 0
        for k , v in sorted(arr , reverse=True):
            s += v
            ans = max(ans , s + k)
        print(f"Case {now}: {ans}")
        now += 1

if __name__ == "__main__":
    main()
