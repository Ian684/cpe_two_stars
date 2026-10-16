def main():
    test = int(input())
    for i in range(test):
        arr = list(map(int , input().split()))
        c = sum(arr)//4-(arr[0]+arr[9])
        a = arr[1]-c
        b = arr[0]-a
        e = arr[8]-c
        d = arr[9]-e
        print(f"Case {i+1}: {a} {b} {c} {d} {e}")

if __name__ == "__main__":
    main()
