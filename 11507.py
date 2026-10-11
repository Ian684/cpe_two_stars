def main():
    while True:
        n = int(input())
        if n <= 1:break
        n -= 1
        now = "+x"
        for command in input().split():
            if command == "No":continue
            if now == "+x":
                now = command
            elif now == "-x":
                if command[0] == '+':
                    now = '-' + command[1]
                else:
                    now = '+' + command[1]
            elif now[1] == command[1]:
                if now[0] == command[0]:
                    now = "-x"
                else:
                    now = "+x"
        print(now)

if __name__ == "__main__":
    main()
