def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        red , blue = [] , []
        for i in range(n):
            temp = int(input())
            if temp < 0:
                red.append(abs(temp))
            else:
                blue.append(temp)
        red , blue = sorted(red , key = lambda x : -x) , sorted(blue , key = lambda x : -x)
        if red[0] > blue[0]:
            flag = "red"
        else:
            flag = "blue"
        now = 1 << 32
        r , b = 0 , 0
        ans = 0
        while True:
            if r < len(red) and flag == "red":
                while r < len(red) and red[r] >= now:
                    r += 1
                if r >= len(red):break
                now = red[r]
                r += 1
                flag = "blue"
            elif b < len(blue) and flag == "blue":
                while b < len(blue) and blue[b] >= now:
                    b += 1
                if b >= len(blue):break
                now = blue[b]
                b += 1
                flag = "red"
            else:break
            ans += 1
        print(ans)

if __name__ == "__main__":
    main()
