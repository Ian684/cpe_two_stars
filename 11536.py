from collections import deque

def main():
    test = int(input())
    for ca in range(test):
        n , m , k = map(int , input().split())
        ans = 1 << 32
        count = [0]*(k+1)
        now = 0
        x = deque([])
        a , b , c = 0 , 0 , 0
        for right in range(n):
            if right <= 2:
                temp = right + 1
            else:
                temp = (a + b + c) % m + 1
            if 1 <= temp <= k:
                if count[temp] == 0:
                    now += 1
                count[temp] += 1
            x.append(temp)
            while now == k:
                ans = min(ans , len(x))
                l = x.popleft()
                if 1 <= l <= k:
                    count[l] -= 1
                    if count[l] == 0:
                        now -= 1
            a , b , c = b , c , temp
        if ans == 1 << 32:
            print(f"Case {ca+1}: sequence nai")
        else:
            print(f"Case {ca+1}: {ans}")

if __name__ == "__main__":
    main()
