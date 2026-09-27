def main():
    while True:
        pilots = []
        try:
            n = int(input())
            for i in range(n):
                line = input().split()
                name = line[0]
                a , b , c = int(line[2]) , int(line[4]) , int(line[6])
                c += a * 60 * 1000 + b * 1000
                pilots.append([c , name])
            pilots = sorted(pilots , key = lambda x : (x[0] , x[1].lower()))
            i = 0
            while i < n:
                print("Row" , i//2+1)
                print(pilots[i][1])
                if i+1 < n:
                    print(pilots[i+1][1])
                i += 2
            print()
            line = input()
        except EOFError:break

if __name__ == "__main__":
    main()
