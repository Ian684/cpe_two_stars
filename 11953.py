from collections import deque

def bfs(n , arr , i , j , check):

    q = deque([])
    q.append([i , j])
    check[i][j] = True
    directions = ((-1,0),(1,0),(0,-1),(0,1))
    
    while q:
        x , y = q.popleft()

        for dx , dy in directions:
            nx , ny = x + dx , y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:continue
            if check[nx][ny]:continue
            if arr[nx][ny] == '.':continue
            check[nx][ny] = True
            q.append([nx , ny])

    return check

def main():
    test = int(input())
    for case in range(test):
        n = int(input())
        arr = []
        for i in range(n):
            arr.append(input())
        check = [[False]*n for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(n):
                if check[i][j]:continue
                if arr[i][j] == '.' or arr[i][j] == '@':continue
                check = bfs(n , arr , i , j , check)
                ans += 1
        print(f"Case {case+1}: {ans}")

if __name__ == "__main__":
    main()
