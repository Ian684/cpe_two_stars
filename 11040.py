def main():
    t = int(input())
    for _ in range(t):
        for i in range(3):
            line = input()
        a = list(map(int , input().split()))
        b = list(map(int , input().split()))
        result = [[0]*9 for i in range(9)]
        for i in range(4):
            result[8][i*2+1] = (a[i] - b[i] - b[i+1]) // 2
            result[8][i*2] = b[i]
        result[8][8] = b[4]
        for i in range(7 , -1 , -1):
            for j in range(i+1):
                result[i][j] = result[i+1][j] + result[i+1][j+1]
        for i in range(9):
            print(' '.join(map(str , result[i][:i+1])))

if __name__ == "__main__":
    main()
