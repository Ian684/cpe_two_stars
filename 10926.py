from collections import deque

def bfs(aim , n , lines):
    
    q = deque([aim])
    check = [False]*n
    check[aim] = True
    result = 0

    while q:
        point = q.popleft()

        for _next in lines[point]:
            if check[_next]:continue
            q.append(_next)
            result += 1
            check[_next] = True
    return result

def main():
    while True:
        n = int(input())
        if n == 0:break
        lines = [[] for _ in range(n)]
        for i in range(n):
            for temp in sorted(list(map(int , input().split()))[1:]):
                lines[i].append(temp-1)
        ans = -1
        m = -1
        for i in range(n):
            now = bfs(i , n , lines)
            if now > m:
                ans = i
                m = now
        print(ans+1)

if __name__ == "__main__":
    main()
