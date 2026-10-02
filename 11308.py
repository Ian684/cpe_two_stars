def main():
    test = int(input())
    for _ in range(test):
        name = input().upper()
        m , n , b = map(int , input().split())
        prices = {}
        for i in range(m):
            ing , c = input().split()
            prices[ing] = int(c)
        result = []
        for i in range(n):
            dish_name = input()
            x = int(input())
            count = 0
            for j in range(x):
                aim , unit = input().split()
                count += prices[aim]*int(unit)
            if count > b:
                continue
            result.append([count , dish_name])
        print(name)
        if len(result) == 0:
            print("Too expensive!")
        else:
            for i , j in sorted(result):
                print(j)
        print()

if __name__ == "__main__":
    main()
