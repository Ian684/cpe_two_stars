def cross(p1 , q1 , p2 , q2):
    return p1*q2-q1*p2

def main():
    while True:
        n = int(input())
        if n == 0:break
        points = []
        ans = set()
        for i in range(n):
            x1 , y1 , x2 , y2 = map(float , input().split())
            for p in list(ans):
                a1 , b1 , a2 , b2 = points[p]
                if cross(x2-x1 , y2-y1 , a1-x1 , b1-y1) * cross(x2-x1 , y2-y1 , a2-x1 , b2-y1) < 0 and cross(a2-a1 , b2-b1 , x1-a1 , y1-b1) * cross(a2-a1 , b2-b1 , x2-a1 , y2-b1) < 0:
                    ans.remove(p)
            points.append([x1 , y1 , x2 , y2])
            ans.add(i)
        ans = sorted(list(ans))
        for a in range(len(ans)):
            ans[a] += 1
        print(f"Top sticks: {', '.join(map(str , ans))}.")

if __name__ == "__main__":
    main()
