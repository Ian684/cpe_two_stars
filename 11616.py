def main():
    values = [1000, 900, 500, 400, 100, 90, 50,
              40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L",
              "XL", "X", "IX", "V", "IV", "I"]

    while True:
        try:
            s = input()
        except EOFError:
            break

        if s.isdigit():
            n = int(s)
            ans = ""
            for i in range(13):
                while n >= values[i]:
                    n -= values[i]
                    ans += romans[i]
        else:
            d = dict(zip(romans, values))
            ans = 0
            i = 0
            while i < len(s):
                if i + 1 < len(s) and s[i:i+2] in d:
                    ans += d[s[i:i+2]]
                    i += 2
                else:
                    ans += d[s[i]]
                    i += 1
        print(ans)

if __name__ == "__main__":
    main()
