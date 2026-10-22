def main():
    while True:
        n = int(input())
        if n == 0:break
        print(n.bit_length()-1)

if __name__ == "__main__":
    main()
