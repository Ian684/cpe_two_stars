import sys

def main():
    input_data = sys.stdin.read().split()
    tokens = iter(input_data)
    while True:
        n , m = int(next(tokens)) , int(next(tokens))
        if n == 0 and m == 0:break
        arr = set()
        for i in range(n):
            arr.add(next(tokens))
        ans = 0
        for i in range(m):
            if next(tokens) in arr:
                ans += 1
        print(ans)

if __name__ == "__main__":
    main()
