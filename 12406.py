def main():
    ans = [[] for _ in range(18)]
    def dfs(now):
        if len(now) >= 18:return
        ans[len(now)].append(int(now))
        dfs(now+'1')
        dfs(now+'2')
    dfs("1")
    dfs("2")
    t = int(input())
    for c in range(t):
        p , q = map(int , input().split())
        aim = 2**q
        result = []
        for a in ans[p]:
            if a % aim == 0:
                result.append(a)
        if len(result) == 0:
            print(f"Case {c+1}: impossible")
        elif len(result) == 1:
            print(f"Case {c+1}: {result[0]}")
        else:
            print(f"Case {c+1}: {min(result)} {max(result)}")

if __name__ == "__main__":
    main()
