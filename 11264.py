def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int , input().split()))
        result = []
        total = 0
        for i in range(n):
            if total >= arr[i]:
                total -= result.pop()
            result.append(arr[i])
            total += arr[i]
        print(len(result))


if __name__ == "__main__":
    main()
