import sys

def main():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n = int(input())
        now = (1 << 26) - 1
        ans = 0

        for i in range(n):
            temp = 0
            for c in input().strip():
                temp |= 1 << (ord(c) - 97)

            if now & temp:
                now &= temp
            else:
                ans += 1
                now = temp

        print(ans)

if __name__ == "__main__":
    main()
