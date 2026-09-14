def main():
    t = int(input())
    for _ in range(t):
        line1 = input()
        line2 = line1
        line1 = line1.split("*")
        line2 = line2.split("+")
        for i in range(len(line1)):
            line1[i] = sum(map(int , line1[i].split("+")))
        for i in range(len(line2)):
            l = line2[i].split("*")
            temp = 1
            for j in map(int , l):
                temp *= j
            line2[i] = temp
        temp = 1
        for j in map(int , line1):
            temp *= j
        line1 = temp
        line2 = sum(map(int , line2))
        print(f"The maximum and minimum are {line1} and {line2}.")

if __name__ == "__main__":
    main()
