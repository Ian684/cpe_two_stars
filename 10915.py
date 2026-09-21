from math import *

def check(sx , sy , sz , x , y , z):

    r = 20000/pi
    a = sqrt(sx**2 + sy**2 + sz**2)
    b = sqrt(a**2 - r**2)

    aim = sqrt((sx-x)**2 + (sy-y)**2 + (sz-z)**2)

    if aim > b:
        return True
    return False

def main():
    while True:
        k , m = map(int , input().split())
        if k == 0 and m == 0:break
        shoot = []
        for i in range(k):
            shoot.append(list(map(float , input().split())))
        ans = 0
        for i in range(m):
            x , y , z = map(float , input().split())
            flag = False
            for j in range(k):
                sx , sy , sz = shoot[j]
                if not check(sx , sy , sz , x , y , z):
                    flag = True
                    break
            if flag:
                ans += 1
        print(ans)

if __name__ == "__main__":
    main()
