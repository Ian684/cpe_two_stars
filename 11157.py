def solve(arr):

    ans = -1
    for i in range(len(arr)):
        start , end = arr[i][0] , arr[i][-1]
        temp = arr[i][1:-1]
        if len(temp) <= 1:
            ans = max(ans , end - start)
            continue
        ans = max(ans , temp[0]-start , temp[1]-start)
        for i in range(2 , len(temp) , 2):
            ans = max(ans , temp[i]-temp[i-2])
            if i + 1 < len(temp):
                ans = max(ans , temp[i+1]-temp[i-1])
        ans = max(ans , end - temp[-1] , end - temp[-2])

    return ans

def main():
    t = int(input())
    for _ in range(t):
        n , l = map(int , input().split())
        arr = [[0]]
        i = 0
        for temp in input().split():
            a , b = temp.split('-')
            b = int(b)
            arr[i].append(b)
            if a == 'B':
                i += 1
                arr.append([b])
        arr[i].append(l)
        ans = solve(arr)
        print(f"Case {_+1}: {ans}")

if __name__ == "__main__":
    main()
