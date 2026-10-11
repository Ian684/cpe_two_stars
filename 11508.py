def main():
    while True:
        line = input()
        if line == "0":break
        line = list(map(int , line.split()))
        if len(line) - 1 < max(line):
            print("Message hacked by the Martians!!!")
            continue
        arr = [-1]*len(line)
        s = set(line)
        x = [-1]*len(line)
        for l in line:
            x[l] += 1
        now = 0
        for i in range(len(line)):
            if i in s:
                arr[i] = i
                continue
            while now < len(x) and x[now] <= 0:
                now += 1
            x[now] -= 1
            arr[i] = now
        print(' '.join(map(str , arr)))

if __name__ == "__main__":
    main()
