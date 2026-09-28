from collections import deque

def solve(m , n , arr , x , y):

    aim = arr[x][y]
    check = [[False]*n for _ in range(m)]
    directions = ((-1,0),(1,0),(0,-1),(0,1))

    def bfs(ax , ay):
        nonlocal aim , check , directions
        q = deque([])
        count = 1
        q.append([ax , ay])
        check[ax][ay] = True

        while q:
            ax , ay = q.popleft()

            for dx , dy in directions:
                nx , ny = ax + dx , ay + dy
                ny %= n
                if nx < 0 or nx >= m:continue
                if check[nx][ny]:continue
                if arr[nx][ny] != aim:continue
                check[nx][ny] = True
                count += 1
                q.append([nx , ny])

        return count

    bfs(x , y)
    ans = 0
    for i in range(m):
        for j in range(n):
            if check[i][j]:continue
            if arr[i][j] != aim:continue
            ans = max(ans , bfs(i , j))

    return ans

def main():
    while True:
        try:
            m , n = map(int , input().split())
            arr = []
            for i in range(m):
                arr.append(input())
            x , y = map(int , input().split())
            line = input()
        except EOFError:break

        ans = solve(m , n , arr , x , y)
        print(ans)

if __name__ == "__main__":
    main()
