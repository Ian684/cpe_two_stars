def main():
    p = [0]*500001
    now = 2
    x = 1
    p[1] = 1
    while now < 500001:
        for i in range(1 , x+1):
            if now + i - 1 < 500001:
                p[now + i - 1] = i*2
        now += x
        x *= 2

    while True:
        n = int(input())
        if n == 0:break
        print(p[n])

if __name__ == "__main__":
    main()
