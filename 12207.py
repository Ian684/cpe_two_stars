from collections import deque

def main():
    now = 0
    while True:
        p, c = map(int, input().split())
        if p == 0 and c == 0:
            break

        q = deque(range(1, min(p, c) + 1))
        result = []

        for _ in range(c):
            temp = input()
            if temp == 'N':
                i = q.popleft()
                result.append(i)
                q.append(i)
            else:
                i = int(temp.split()[1])
                if i in q:
                    q.remove(i)
                q.appendleft(i)

        print(f"Case {now+1}:")
        now += 1
        for r in result:
            print(r)

if __name__ == "__main__":
    main()
