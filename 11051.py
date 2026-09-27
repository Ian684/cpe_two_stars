def main():
    while True:
        n = int(input())
        if n == 0:break
        r = 0
        flag = 1
        for action in input().split():
            d = int(action[1:])
            if action[0] == 'r':
                r += flag * d
            elif d & 1:
                flag *= -1
        r %= n
        if flag == 1:
            if r == 0:
                print()
            elif n - r + 2 < r:
                print(f"m1 r{n-r} m1")
            else:
                print(f"r{r}")
        elif flag == -1:
            if r == 0:
                print(f"m1")
            elif n - r < r:
                print(f"m1 r{n-r}")
            else:
                print(f"r{r} m1")

if __name__ == "__main__":
    main()
