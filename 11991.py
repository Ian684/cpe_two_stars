def main():
    while True:
        try:
            n , q = map(int , input().split())
            his = {}
            now = 1
            for i in list(map(int , input().split())):
                if i not in his:
                    his[i] = []
                his[i].append(now)
                now += 1
            for i in range(q):
                count , aim = map(int , input().split())
                if count-1 < len(his[aim]):
                    print(his[aim][count-1])
                else:
                    print(0)
        except EOFError:break

if __name__ == "__main__":
    main()
