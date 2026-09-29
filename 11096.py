from math import *

def dis(a , b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def cross(a , b , c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

def solve(n , points):

    if n == 1:
        return 0
    if n == 2:
        return 2*dis(points[0] , points[1])

    points = sorted(points)
    hull = []
    
    for p in points:
        while len(hull) >= 2 and cross(hull[-2] , hull[-1] , p) <= 0:
            hull.pop()
        hull.append(p)

    lower_size = len(hull)
    for p in points[::-1]:
        while len(hull) > lower_size and cross(hull[-2] , hull[-1] , p) <= 0:
            hull.pop()
        hull.append(p)
    hull.pop()

    ans = 0
    for i in range(len(hull)):
        j = (i+1)%len(hull)
        ans += dis(hull[i] , hull[j])
    return ans

def main():
    t = int(input())
    for _ in range(t):
        initial , n = map(int , input().split())
        points = []
        for i in range(n):
            points.append(list(map(int , input().split())))
        line = input()
        ans = solve(n , points)
        print(f"{max(initial , ans):.5f}")

if __name__ == "__main__":
    main()
