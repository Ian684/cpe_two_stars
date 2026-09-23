from math import *

def main():
    while True:
        n = int(input())
        if n == 0:break

        total = float(input().split()[0])
        x , y = 0 , total
        angle = pi / 2
        for i in range(n-1):
            dis , time = input().split()

            dis = float(dis)
            total += dis

            a1 , time = time.split('d')
            a2 , time = time.split('\'')
            a3 = time[:-1]
            angle += pi - (float(a1) + float(a2) / 60 + float(a3) / 3600) * pi / 180
    
            x += dis * cos(angle)
            y += dis * sin(angle)

        result = sqrt(x**2 + y**2)
        if result < total * 0.001:
            print("Acceptable")
        else:
            print("Not acceptable")

if __name__ == "__main__":
    main()
