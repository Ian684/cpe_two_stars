def main():
    test = int(input())
    for _ in range(test):
        n , m = map(int , input().split())
        arr = []
        for i in range(n):
            arr.append(list(map(int , input().split())))
        if m == 0:
            print("Yes")
            continue
        check = set()
        flag = True
        for j in range(m):
            count = 0
            temp = []
            for i in range(n):
                count += arr[i][j]
                temp.append(arr[i][j])
            temp = tuple(temp)
            if temp in check or count != 2:
                flag = False
                break
            check.add(temp)
        if flag:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
