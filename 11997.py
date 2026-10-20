from heapq import *

def merge(arr , temp , n):
    temp.sort()
    q = []

    for i in  range(n):
        heappush(q , [arr[i] + temp[0] , i , 0])

    result = []
    for _ in range(n):
        count , i , j = heappop(q)
        result.append(count)
        if j + 1 < n:
            heappush(q , [arr[i]+temp[j+1] , i , j+1])

    return result

def main():
    while True:
        try:
            n = int(input())
            arr = sorted(list(map(int , input().split())))
            for i in range(n-1):
                temp = sorted(list(map(int , input().split())))
                arr = merge(arr , temp , n)
            print(*arr)
        except EOFError:break
if __name__ == "__main__":
    main()
