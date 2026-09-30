from math import *

st = []
group = []
start = []
end = []

def query(i , j):
    global st , group

    i , j = group[i]+1 , group[j]-1
    if i > j:
        return 0
    l = int(log(j-i+1 , 2))
    return max(
        st[l][i],
        st[l][j-2**l+1]
    )

def generate_st(line):
    global st , group , start , end

    group = [None]*len(line)
    start = []
    end = []
    last = line[0]
    arr = [1]
    now = 0
    start.append(0)

    for i in range(len(line)):
        if line[i] == last:
            arr[-1] += 1
            group[i] = now
        else:
            end.append(i-1)
            arr.append(1)
            now += 1
            group[i] = now
            start.append(i)
            last = line[i]

    end.append(len(line)-1)
    n = len(arr)
    l = int(log(n,2))+1
    st = [[0]*n for _ in range(l)]
    for i in range(n):
        st[0][i] = arr[i]
    for k in range(1,l):
        for i in range(n-2**k+1):
            st[k][i] = max(
                st[k-1][i],
                st[k-1][i+2**(k-1)]
            )

def main():

    while True:
        line = input()
        if line == '0':break
        n , q = map(int,line.split())
        line = list(map(int,input().split()))
        generate_st(line)
        for _ in range(q):
            i,j = map(int,input().split())
            i -= 1
            j -= 1
            if line[i] == line[j]:
                ans = j-i+1
            else:
                left = end[group[i]] - i + 1
                right = j - start[group[j]] + 1
                ans = max(
                    left,
                    right,
                    query(i,j)
                )
            print(ans)

if __name__ == "__main__":
    main()
