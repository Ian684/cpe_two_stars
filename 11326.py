from math import *

def main():
    esp = 1e-8
    test = int(input())
    for _ in range(test):
        l , w , cita = map(int , input().split())
        cita = cita * pi / 180
        if sin(cita) == 0:
            print("1.000")
            continue
        r = w / sin(cita)
        base = sqrt(r**2 - w**2)
        times = int(l // base)
        remain = l % base
        remain_r = remain / sin(pi/2 - cita)
        remain_w = sqrt(remain_r**2 - remain**2)
        if times & 1:
            remain_w = w - remain_w
        B = sqrt(remain_w**2 + l**2)
        A = r * times + remain_r
        ans = f"{A/B:.3f}"
        print(ans)

if __name__ == "__main__":
    main()
