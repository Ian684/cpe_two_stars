def main():
    t = int(input())
    for c in range(t):
        l , t , n = map(int , input().split())
        arr = []
        result = []
        for i in range(n):
            pos , direction = input().split()
            pos = int(pos)
            if direction == "R":
                result.append([pos + t , direction])
            else:
                result.append([pos - t , direction])
            arr.append([i , pos , direction])
        arr = sorted(arr , key = lambda x : x[1])
        result = sorted(result)
        his = {}
        for i in range(n):
            arr[i][1] = result[i][0]
            arr[i][2] = result[i][1]
            if result[i][0] not in his:
                his[result[i][0]] = 0
            his[result[i][0]] += 1
        arr = sorted(arr , key = lambda x : x[0])
        print(f"Case #{c+1}:")
        for i, pos , d in arr:
            if pos > l or pos < 0:
                print("Fell off")
            elif his[pos] >= 2:
                print(pos , "Turning")
            else:
                print(pos , d)
        print()

if __name__ == "__main__":
    main()
