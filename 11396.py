from collections import deque

def bfs(n , lines):
    
    q = deque([])
    q.append([0 , 1])
    check = [0]*n
    check[0] = 1
    while q:
        now , cato = q.popleft()

        for _next in lines[now]:
            if check[_next]:
                if check[_next] == check[now]:
                    return False
            else:
                check[_next] = -1*cato
                q.append([_next , -1*cato])
    return True
    

def main():
    while True:
        n = int(input())
        if n == 0:break
        lines = {}
        while True:
            a , b = map(int , input().split())
            if a == 0 and b == 0:break
            a -= 1
            b -= 1
            if a not in lines:
                lines[a] = []
            if b not in lines:
                lines[b] = []
            lines[a].append(b)
            lines[b].append(a)
        if bfs(n , lines):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
