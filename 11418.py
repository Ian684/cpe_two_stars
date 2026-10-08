def solve(n , lines):

    match_n = [-1]*n
    ans = [""]*n

    def dfs(now , check):
        for _next , word in lines[now]:
            if check[_next]:continue
            check[_next] = True
            if match_n[_next] == -1 or dfs(match_n[_next] , check):
                match_n[_next] = now
                ans[_next] = word
                return True
        return False

    for u in range(n):
        check = [False]*n
        dfs(u , check)

    return ans



def main():
    t = int(input())
    for c in range(t):
        n = int(input())
        lines = []
        for i in range(n):
            line = input().split()
            lines.append([])
            for l in line[1:]:
                if ord(l[0].upper())-65 >= n:continue
                lines[-1].append([ord(l[0].upper())-65 , l])
        ans = solve(n , lines)
        print(f"Case #{c+1}:")
        for a in ans[:n]:
            print(a.capitalize())

if __name__ == "__main__":
    main()
