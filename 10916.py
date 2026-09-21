from math import *

def main():
    bit = []
    b = 4
    for i in range(21):
        bit.append(b)
        b *= 2
    ans = []
    temp = 0
    aim = 0
    now = 1
    while aim < len(bit):
        if ceil(temp + log(now , 2)) > bit[aim]:
            ans.append(now-1)
            aim += 1
        temp += log(now , 2)
        now += 1

    while True:
        y = int(input())
        if y == 0:break
        y = (y-1960)//10
        print(ans[y])

if __name__ == "__main__":
    main()
