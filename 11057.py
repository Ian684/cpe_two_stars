def main():
    while True:
        try:
            n = int(input())
            arr = list(map(int , input().split()))
            check = {}
            for a in arr:
                if a not in check:
                    check[a] = 0
                check[a] += 1
            w = int(input())
            line = input()
        except EOFError:break
        
        ans = None
        plus = 1 << 32

        for a in arr:
            aim = w - a
            if aim not in check:continue
            if a == aim:
                if check[aim] >= 2:
                    ans = a
                    plus = 0
                    break
            else:
                if abs(aim - a) < plus:
                    ans = min(aim , a)
                    plus = abs(aim - a)
        print(f"Peter should buy books whose prices are {ans} and {ans+plus}.")
        print()
                    
if __name__ == "__main__":
    main()
