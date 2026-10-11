from math import *

def cal(n , arr):

    x , y = 0 , 0
    cita = 0
    for i in range(len(arr)):
        a , b = arr[i]
        if a == 'b' or a == 'f':
            if a == 'b':
                b *= -1
            x += cos(cita)*b
            y += sin(cita)*b
        elif a == 'l':
            cita += b / 180 * pi
        elif a == 'r':
            cita -= b / 180 * pi
    return x , y , cita

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = []
        aim = None
        for i in range(n):
            a , b = input().split()
            a = a[0]
            if b == '?':
                aim = i
                b = 0
            b = int(b)
            arr.append([a , b])
        if arr[aim][0] == 'f' or arr[aim][0] == 'b':
            x , y , cita = cal(n , arr)
            print(round(hypot(x , y)))
        else:
            for angle in range(360):
                arr[aim][1] = angle
                x , y , cita = cal(n , arr)
                if hypot(x , y) < 1e-6:
                    print(angle)
                    break

if __name__ == "__main__":
    main()
