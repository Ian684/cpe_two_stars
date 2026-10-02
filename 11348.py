def main():
    test = int(input())
    for c in range(test):
        n = int(input())
        his = {}
        people = []
        for i in range(n):
            line = list(map(int , input().split()))
            m , line = line[0] , line[1:]
            line = list(set(line))
            people.append(line)
            for l in line:
                if l not in his:
                    his[l] = 0
                his[l] += 1
        ans = []
        total = 0
        for p in people:
            count = 0
            for i in p:
                if his[i] >= 2:continue
                count += 1
            total += count
            ans.append(count)

        print(f"Case {c+1}:" , end="")
        for i in ans:
            if total == 0:
                print(f" {0:.6f}%" , end="")
                continue
            print(f" {i/total*100:.6f}%" , end="")
        print()

if __name__ == "__main__":
    main()
