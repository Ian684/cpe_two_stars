def main():
    while True:
        h , w = map(int , input().split())
        if h == 0 and w == 0:break
        line = list(map(int , input().split()))
        ans = h - line[0]
        for i in range(w-1):
            j = i + 1
            if line[i] > line[j]:
                ans += line[i] - line[j]
        print(ans)


if __name__ == "__main__":
    main()
