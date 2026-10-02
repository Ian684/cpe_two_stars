def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        i = 1
        ans = 0
        for a in sorted(list(map(int , input().split())) , reverse=True):
            if i % 3 == 0:
                ans += a
            i += 1
        print(ans)

if __name__ == "__main__":
    main()
