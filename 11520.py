def check(arr , i , j , x):

    directions = ((-1,0),(1,0),(0,-1),(0,1))
    
    for dx , dy in directions:
        nx , ny = dx + i , dy + j
        if nx < 0 or ny < 0 or nx >= len(arr) or ny >= len(arr):continue
        if arr[nx][ny] == x:
            return False
    return True

def main():

    alph = []
    for i in range(26):
        alph.append(chr(65+i))

    test = int(input())
    for c in range(test):
        n = int(input())
        arr = []
        for i in range(n):
            arr.append(list(input()))
        for i in range(n):
            for j in range(n):
                if arr[i][j] != '.':continue
                for x in alph:
                    if not check(arr , i , j , x):continue
                    al = x
                    break
                arr[i][j] = al
        print(f"Case {c+1}:")
        for a in arr:
            print(''.join(a))

if __name__ == "__main__":
    main()
