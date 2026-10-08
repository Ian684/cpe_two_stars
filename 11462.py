def main():
    while True:
        if input() == '0':break
        print(' '.join(map(str , sorted(list(map(int , input().split()))))))

if __name__ == "__main__":
    main()
