def main():
    while True:
        n = int(input())
        if n == 0:break
        arr = [0]
        for i in range(n):
            arr.append(int(input()))
        arr = sorted(arr)
        flag = True
        for i in range(n):
            j = i + 1
            if arr[j] - arr[i] <= 200:continue
            flag = False
            break
        if flag and (1422 - arr[-1])*2 > 200:
            flag = False
        if flag:
            print("POSSIBLE")
        else:
            print("IMPOSSIBLE")

if __name__ == "__main__":
    main()
