def main():
    now = 1
    while True:
        n = input()
        if n == "":continue
        n = int(n)
        if n == 0:break
        lines = {}
        parents = []
        result = None
        for i in range(n):
            temp = input()
            if temp == "</n>":
                temp = parents.pop()
                if temp not in lines:
                    lines[temp] = [None , []]
                if len(parents) == 0:
                    result = temp
                    break
                if parents[-1] not in lines:
                    lines[parents[-1]] = [None , []]
                lines[temp][0] = parents[-1]
                lines[parents[-1]][1].append(temp)
            else:
                temp = temp.split('\'')[1]
                parents.append(temp)
        q = int(input())
        print(f"Case {now}:")
        now += 1
        for i in range(q):
            command = input()
            if command == "first_child":
                if len(lines[result][1]) != 0:
                    result = lines[result][1][0]
            elif command == "next_sibling":
                parent = lines[result][0]
                if parent is not None:
                    f = lines[parent][1].index(result)+1
                    if f < len(lines[parent][1]):
                        result = lines[parent][1][f]
            elif command == "previous_sibling":
                parent = lines[result][0]
                if parent is not None:
                    f = lines[parent][1].index(result)-1
                    if f >= 0:
                        result = lines[parent][1][f]
            elif command == "parent":
                if lines[result][0] is not None:
                    result = lines[result][0]
            print(result)
                
if __name__ == "__main__":
    main()
