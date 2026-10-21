def main():
    test = int(input())
    for _ in range(test):
        n = int(input())
        arr = list(map(int , input().split()))
        q = int(input())
        for i in range(q):
            a , b = map(int , input().split())
            temp = arr[a-1:b]
            temp = sorted(temp)
            ans = 1 << 32
            for j in range(len(temp)-1):
                ans = min(ans , temp[j+1]-temp[j])
            print(ans)

if __name__ == "__main__":
    main()
