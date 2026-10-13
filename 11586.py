def main():
    t = int(input())
    for _ in range(t):
        line = input().split()
        if len(line) == 1:
            print("NO LOOP")
            continue
        if line.count("MM") == line.count("FF"):
            print("LOOP")
        else:
            print("NO LOOP")

if __name__ == "__main__":
    main()
