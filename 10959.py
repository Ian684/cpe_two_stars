from collections import deque

def bfs(aim , p , dances):
    q = deque([])
    q.append([aim , 0])
    check = [False]*p
    check[aim] = True

    while q:
        point , step = q.popleft()

        for _next in dances[point]:
            if check[_next]:continue
            if _next == 0:return step + 1
            check[_next] = True
            q.append([_next , step + 1])
    
    return None

def main():
    t = int(input())
    for _ in range(t):
        line = input()
        p , d = map(int , input().split())
        dances = {}
        for i in range(d):
            a , b = map(int , input().split())
            if a not in dances:
                dances[a] = set()
            if b not in dances:
                dances[b] = set()
            dances[a].add(b)
            dances[b].add(a)

        for aim in range(1 , p):
            ans = bfs(aim , p , dances)
            print(ans)

        if _ != t - 1:print()

if __name__ == "__main__":
    main()
