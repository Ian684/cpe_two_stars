def main():
    while True:
        n = int(input())
        if n == 0:break
        lines = {}
        for i in range(n):
            a , b = map(int , input().split())
            if (a , b) in lines:
                lines[(a , b)] += 1
            else:
                if (b , a) in lines:
                    lines[(b , a)] -= 1
                else:
                    lines[(a , b)] = 1
        flag = True
        for k , v in lines.items():
            if v != 0:
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
