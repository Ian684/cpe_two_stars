def main():
    his = {}
    n = int(input())
    for _ in range(n):
        a = input()
        b = input()
        his[a] = b
    q = int(input())
    for _ in range(q):
        a = input()
        print(his[a])
        
if __name__ == "__main__":
    main()
