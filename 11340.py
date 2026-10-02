def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        prices = {}
        for i in range(n):
            name , p = input().split()
            prices[name] = int(p)
        q = int(input())
        ans = 0
        for i in range(q):
            line = input()
            for l in line:
                if l not in prices:
                    continue
                ans += prices[l]
        print(f"{ans/100:.2f}$")

if __name__ == "__main__":
    main()
