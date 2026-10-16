def main():
    test = int(input())
    for _ in range(test):
        count = {}
        for l in input():
            if l == ' ':continue
            if l not in count:
                count[l] = 0
            count[l] += 1
        i = 2
        now = 1
        m = 2
        ans = 0
        flag = 1
        for k , v in sorted(count.items() , key = lambda x : -x[1]):
            ans += i*v
            now += 1
            if now >= m:
                now = 1
                i += 1
                m += flag
                if m >= 7:
                    flag = -1

        print(ans)

if __name__ == "__main__":
    main()
