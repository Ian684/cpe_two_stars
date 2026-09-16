def main():
    ans = set()
    alph = set()
    for i in range(26):
        alph.add(chr(97 + i))
    while True:
        try:
            line = input()
            if line == "":continue
        except EOFError:break
        temp = ""
        for char in line.lower():
            if char not in alph:
                ans.add(temp)
                temp = ""
            else:
                temp += char
        ans.add(temp)

    for i in sorted(list(ans)):
        if i == "":continue
        print(i)

if __name__ == "__main__":
    main()
