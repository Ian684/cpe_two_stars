def main():
    test = int(input())
    for _ in range(test):
        temp = input()
        m = int(temp)
        flag = True
        for l in list(map(int , input().split()))[1:]:
            if m % l != 0:
                flag = False
                break
        if flag:
            print(f"{temp} - Wonderful.")
        else:
            print(f"{temp} - Simple.")

if __name__ == "__main__":
    main()
