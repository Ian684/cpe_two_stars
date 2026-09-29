def main():
    while True:
        n , d = map(int , input().split())
        if n == 0 and d == 0:break
        print(n**d)

if __name__ == "__main__":
    main()
