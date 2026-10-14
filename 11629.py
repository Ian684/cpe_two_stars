def main():
    p , g = map(int , input().split())
    his = {}
    for i in range(p):
        name , t = input().split()
        his[name] = int(t.replace(".", ""))
    for i in range(g):
        line = input().split()
        aim = int(line[-1])*10
        comp = line[-2]
        line = line[:-2]
        count = 0
        for l in line:
            if l == '+':continue
            count += his[l]
        flag = False
        if comp == "<" and aim - count > 0:flag = True
        elif comp == ">" and count - aim > 0:flag = True
        elif comp == "<=" and aim - count >= 0:flag = True
        elif comp == ">=" and count - aim >= 0:flag = True
        elif comp == "=" and count == aim:flag = True
        if flag:
            print(f"Guess #{i+1} was correct.")
        else:
            print(f"Guess #{i+1} was incorrect.")

if __name__ == "__main__":
    main()
