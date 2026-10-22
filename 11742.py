def solve(n , m , res):

    ans = 0
    choose = set(range(n))
    def check(now , res):
        for k , v in res.items():
            a , b = k
            for c in v:
                if c < 0 and abs(now[a] - now[b]) >= -c:continue
                if c > 0 and abs(now[a] - now[b]) <= c:continue
                return False
        return True

    def dfs(now , idx):
        nonlocal ans , choose
        if idx == n:
            if check(now , res):
                ans += 1
            return 
        for ch in list(choose):
            choose.remove(ch)
            now[ch] = idx
            dfs(now , idx+1)
            now[ch] = None
            choose.add(ch)

    dfs({} , 0)
    return ans



def main():
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:break
        res = {}
        for i in range(m):
            a , b , c = map(int , input().split())
            if a > b:
                a , b = b , a
            if (a , b) not in res:
                res[(a , b)] = []
            res[(a , b)].append(c)
        ans = solve(n , m , res)
        print(ans)

if __name__ == "__main__":
    main()
