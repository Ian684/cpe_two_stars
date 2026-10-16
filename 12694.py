from collections import deque

def bfs(lines):
    
    q = deque([])
    q.append([0 , 0])
    ans = 0

    while q:
        after , count = q.popleft()
        ans = max(count , ans)

        for a , b in lines:
            if after <= a:
                q.append([b , count + 1])
    return ans


def main():
    n = int(input())
    for _ in range(n):
        lines = []
        while True:
            a , b = map(int , input().split())
            if a == 0 and b == 0:break
            lines.append([a , b])
        ans = bfs(lines)
        print(ans)

if __name__ == "__main__":
     main()
