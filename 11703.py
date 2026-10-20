from math import *

def main():

    x = [1]
    for i in range(1 , 1000000):
        x.append((x[int(i-sqrt(i))] + x[int(log(i))] + x[int(i*(sin(i)**2))]) % 1000000)

    while True:
        n = int(input())
        if n == -1:break
        print(x[n])

if __name__ == "__main__":
    main()
