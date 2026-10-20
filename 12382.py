def main():
    test = int(input())
    for _ in range(test):
        m , n = map(int , input().split())
        col1 = list(map(int , input().split()))
        row1 = list(map(int , input().split()))
        ans1 = sum(col1)
        for r in row1:
            i = 0
            temp = r
            col1 = sorted(col1 , reverse=True)
            while temp > 0 and i < m:
                if col1[i] > 0:
                    col1[i] -= 1
                    temp -= 1
                i += 1
            ans1 += temp
        print(ans1)

if __name__ == "__main__":
    main()
