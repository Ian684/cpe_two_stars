def main():
    t = int(input())
    for now in range(t):
        n = int(input())
        line = []
        while len(line) < n*2:
            line += list(map(int , input().split()))
        arr = []
        for i in range(n):
            arr.append(line[i]-line[i+n])
        count = 0
        m = 0
        flag = True
        for i in range(n):
            if count + arr[i] < 0:
                m = i+1
                count = 0
            else:
                count += arr[i]
        if m != n:
            for i in range(m):
                if count + arr[i] < 0:
                    flag = False
                    break
                else:
                    count += arr[i]
        else:flag = False
        print(f"Case {now+1}: " , end="")
        if flag:
            print(f"Possible from station {m+1}")
        else:
            print("Not possible")

if __name__ == "__main__":
    main()
