def main():
    test = int(input())
    for _ in range(test):
        now = [[0 , 1] , [1 , 1] , [1 , 0]]
        for l in input():
            if l == 'L':
                now = [now[0] , [now[0][0]+now[1][0] , now[0][1]+now[1][1]] , now[1]]
            else:
                now = [now[1] , [now[1][0]+now[2][0] , now[1][1]+now[2][1]] , now[2]]
        print(f"{now[1][0]}/{now[1][1]}")

if __name__ == "__main__":
    main()
