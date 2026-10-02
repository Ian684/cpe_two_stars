from math import *

def main():
    while True:
        try:
            a , u , v = map(int , input().split())
        except EOFError:break
        if a == 0:
            k = 0
        else:
            k = max(2*v-1 , ceil(((2*u-1)+sqrt((1-2*u)**2+8*a))/2))
        print(k)
if __name__ == "__main__":
    main()
