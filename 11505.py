from math import *

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        x , y = 0 , 0
        cita = 0
        for i in range(n):
            a , b = input().split()
            b = int(b)
            a = a[0]
            if a == 'b' or a == 'f':
                if a == 'b':
                    b *= -1
                x += cos(cita)*b
                y += sin(cita)*b
            elif a == 'l':
                cita += b / 180 * pi
            elif a == 'r':
                cita -= b / 180 * pi
        ans = round(sqrt(x ** 2 + y ** 2))
        print(ans)

if __name__ == "__main__":
    main()
