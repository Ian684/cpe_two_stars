def main():
    while True:
        n = int(input())
        if n == 0:break
        arr = {}
        for i in range(n):
            temp = tuple(sorted(list(map(int , input().split()))))
            if temp not in arr:
                arr[temp] = 0
            arr[temp] += 1
        m = -1
        ans = 0
        for classes , people in arr.items():
            if people == m:
                ans += people
            elif people > m:
                ans = people
                m = people
        print(ans)

if __name__ == "__main__":
    main()
