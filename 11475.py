def generate_lps(p):
    lps = [0]*len(p)
    length = 0
    i = 1

    while i < len(p):
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length-1]
        else:
            lps[i] = 0
            i += 1

    return lps

def main():
    while True:
        try:
            p = input()
        except EOFError:break
        lps = generate_lps(p[::-1] + '#' + p)
        k = lps[-1]
        print(p+p[::-1][k:])

if __name__ == "__main__":
    main()

