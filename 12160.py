from collections import deque

def bfs(start , end , n , arr):

    q = deque([])
    q.append([start , 0])
    check = set()
    ans = 1 << 32

    while q:
        now , count = q.popleft()
        for a in arr:
            temp = (now + a)%10000
            if temp in check:continue
            if temp == end:
                ans = min(ans , count+1)
                continue
            check.add(temp)
            q.append([temp , count + 1])
    if ans == 1 << 32:
        return None
    return ans

def main():
    now = 0
    while True:
        start , end , n = map(int , input().split())
        if start == 0 and end == 0 and n == 0:break
        arr = list(map(int , input().split()))
        ans = bfs(start , end , n , arr)
        if ans is None:
            print(f"Case {now+1}: Permanently Locked")
        else:
            print(f"Case {now+1}: {ans}")
        now += 1

if __name__ == "__main__":
    main()
