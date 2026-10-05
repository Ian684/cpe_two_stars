def main():
    blank = False
    while True:
        a , b = input().split()
        if a == '0' and b == '0':break
        result = bin(int(a , 2) * int(b , 2))[2:]
        second = len(result)
        first = max(len(a) , len(b))
        l = second
        if blank:print()
        else:blank = True
        print(' '*(l-len(a))+a)
        print(' '*(l-len(b))+b)
        print(' '*(l-first)+'-'*first)
        for i in range(len(b) - 1 , -1 , -1):
            if b[i] == '0':
                temp = '0'*len(a)
            else:
                temp = a
            print(' '*(l-len(a))+temp)
            l -= 1
        print('-'*second)
        print(result)

if __name__ == "__main__":
    main()
