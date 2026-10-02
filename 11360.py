n = None
arr = []

def row(a , b):
    global n , arr
    for j in range(n):
        arr[a][j] , arr[b][j] = arr[b][j] , arr[a][j]
    return

def col(a , b):
    global n , arr
    for i in range(n):
        arr[i][a] , arr[i][b] = arr[i][b] , arr[i][a]
    return

def inc():
    global n , arr
    for i in range(n):
        for j in range(n):
            arr[i][j] += 1
            arr[i][j] %= 10
    return 

def dec():
    global n , arr
    for i in range(n):
        for j in range(n):
            arr[i][j] -= 1
            arr[i][j] %= 10
    return 

def transpose():
    global n , arr
    for i in range(n):
        for j in range(i+1):
            arr[i][j] , arr[j][i] = arr[j][i] , arr[i][j]
    return 

def main():
    global n , arr
    test = int(input())
    for c in range(test):
        n = int(input())
        arr = []
        for i in range(n):
            arr.append([])
            for j in input():
                arr[-1].append(int(j))
        q = int(input())
        for i in range(q):
            command = input()
            if len(command) == 3:
                if command == "inc":
                    inc()
                else:
                    dec()
            elif command == "transpose":
                transpose()
            else:
                command , a , b = command.split()
                a , b = int(a) - 1 , int(b) - 1
                if command == "row":
                    row(a , b)
                else:
                    col(a , b)
        print(f"Case #{c+1}")
        for i in range(n):
            print(''.join(map(str , arr[i])))
        print()

if __name__ == "__main__":
    main()
