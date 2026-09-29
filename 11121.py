def main():
    t = int(input())
    for c in range(t):
        n = int(input())
        if n == 0:ans = '0'
        else:
            ans = ""
            while n != 0:
                r = n % 2
                ans += str(r)
                n = (n - r) // -2
        print(f"Case #{c+1}: {ans[::-1]}")

if __name__ == "__main__":
    main()
