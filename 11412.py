def solve(aim , to):
    n1 , n2 = 0 , 0
    if aim[0] == to[0]:
        n1 += 1
    elif aim[0] in to:
        n2 += 1
    if aim[1] == to[1]:
        n1 += 1
    elif aim[1] in to:
        n2 += 1
    if aim[2] == to[2]:
        n1 += 1
    elif aim[2] in to:
        n2 += 1
    if aim[3] == to[3]:
        n1 += 1
    elif aim[3] in to:
        n2 += 1
    return n1 , n2

def generate():

    colors = ['R' , 'G' , 'B' , 'Y' , 'O' , 'V']
    check = set()
    total = set()
    def dfs(now):
        nonlocal total , colors
        if len(check) >= 4:
            total.add(now)
            return
        for col in colors:
            if col in check:continue
            check.add(col)
            dfs(now+col)
            check.remove(col)
        return

    dfs('')
    return total

def main():
    total = generate()
    test = int(input())
    for c in range(test):
        line = input()
        aim , n1 , n2 = input().split()
        n1 , n2 = int(n1) , int(n2)
        valid = set()
        for to in total:
            r1 , r2 = solve(aim , to)
            if r1 == n1 and r2 == n2:
                valid.add(to)
        aim , n1 , n2 = input().split()
        n1 , n2 = int(n1) , int(n2)
        flag = False
        for to in valid:
            r1 , r2 = solve(aim , to)
            if r1 == n1 and r2 == n2:
                flag = True
                break
        if flag:
            print("Possible")
        else:
            print("Cheat")

if __name__ == "__main__":
    main()
            




