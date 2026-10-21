from math import *

def main():
    while True:
        try:
            n = int(input())
            print(n-1+ceil(log(n , 2))-1)
        except EOFError:break

if __name__ == "__main__":
    main()
