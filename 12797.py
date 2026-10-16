from collections import deque

def bfs(n, arr):
    directions = ((-1,0),(1,0),(0,-1),(0,1))
    ans = float('inf')

    for mask in range(1 << 10):

        start = arr[0][0]
        end = arr[n-1][n-1]

        if ((mask >> (start % 10)) & 1) != (start < 10):
            continue
        if ((mask >> (end % 10)) & 1) != (end < 10):
            continue

        q = deque([(0, 0, 1)])
        check = [[False] * n for _ in range(n)]
        check[0][0] = True

        while q:
            x, y, count = q.popleft()

            if count >= ans:
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                if check[nx][ny]:
                    continue

                v = arr[nx][ny]

                if ((mask >> (v % 10)) & 1) == 0 and v < 10:
                    continue
                if ((mask >> (v % 10)) & 1) == 1 and v >= 10:
                    continue

                if nx == n-1 and ny == n-1:
                    ans = min(ans, count + 1)
                    break

                check[nx][ny] = True
                q.append((nx, ny, count + 1))

            if ans <= count + 1:
                break

        if ans == 2*n - 1:
            break

    return ans if ans != float('inf') else None


def main():
    alph = {}
    for i in range(10):
        alph[chr(65+i)] = i
        alph[chr(97+i)] = i+10

    while True:
        try:
            n = int(input())
            arr = []
            for i in range(n):
                temp = input()
                arr.append([])
                for j in range(n):
                    arr[-1].append(alph[temp[j]])
        except EOFError:
            break

        ans = bfs(n, arr)
        if ans is None:
            print(-1)
        else:
            print(ans)


if __name__ == "__main__":
    main()
