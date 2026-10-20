def main():
    while True:
        try:
            n = int(input())
            arr = []
            total = 0
            for i in range(n):
                temp = sorted(list(map(int , input().split())))
                total += temp[0]
                arr.append(temp[1]-temp[0])
        except EOFError:break
        print(f"{total}" , end='')
        arr = sorted(arr)
        for i in range(n-1):
            print(f" {total+arr[i]}" , end='')
        print()

if __name__ == "__main__":
    main()
