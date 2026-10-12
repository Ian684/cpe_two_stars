def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        if n > m:
            n, m = m, n
        print((n * m * (n + m - 2)) + 2 * n * (n - 1) * (3 * m - n - 1) // 3)

if __name__ == "__main__":
    main()
