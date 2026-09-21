from math import *

def main():
    while True:
        size , n = map(int , input().split())
        if size == 0 and n == 0:break
        stage = int(sqrt(n))
        if not (stage & 1):
            stage -= 1
        times = n - stage ** 2
        x = (stage - 1) // 2 + size // 2 + 1
        y = (stage - 1) // 2 + size // 2 + 1
        if times > 0:
            x += 1
            times -= 1
        if times > 0 and times <= stage:
            y -= times
            times = 0
        if times > 0 and times > stage:
            y -= stage
            times -= stage
        if times > 0 and times <= stage + 1:
            x -= times
            times = 0
        if times > 0 and times > stage + 1:
            x -= stage + 1
            times -= stage + 1
        if times > 0 and times <= stage + 1:
            y += times
            times = 0
        if times > 0 and times > stage + 1:
            y += stage + 1
            times -= stage + 1
        if times > 0:
            x += times
            times = 0
        print(f"Line = {x}, column = {y}.")

if __name__ == "__main__":
    main()
