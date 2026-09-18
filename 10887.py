def main():
    t = int(input())
    for c in range(t):
        m , n = map(int , input().split())
        his = set()
        for i in range(m):
            his.add(input())
        ans = set()
        for i in range(n):
            temp = input()
            for j in his:
                ans.add(j + temp)
        print(f"Case {c + 1}: {len(ans)}")

if __name__ == "__main__":
    main()
