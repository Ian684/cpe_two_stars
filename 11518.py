from collections import *

def bfs(n , lines , start , check):
    q = deque([])
    q.append(start)

    while q:
        now = q.popleft()
        
        for _next in lines[now]:
            if check[_next]:continue
            check[_next] = True
            q.append(_next)

    return check

def main():
    test = int(input())
    for _ in range(test):
        n , m , l = map(int , input().split())
        lines = [[] for i in range(n)]
        for i in range(m):
            a , b = map(int , input().split())
            a -= 1
            b -= 1
            lines[a].append(b)
        check = [False]*n
        for i in range(l):
            start = int(input())
            start -= 1
            if check[start]:continue
            check[start] = True
            check = bfs(n , lines , start , check)
        print(sum(check))

if __name__ == "__main__":
    main()
