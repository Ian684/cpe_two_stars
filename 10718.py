def main():
    while True:
        try:
            n , low , high = map(int , input().split())
        except EOFError:break

        nb = bin(n)[2:].zfill(32)
        lb = bin(low)[2:].zfill(32)
        hb = bin(high)[2:].zfill(32)
        i = 0
        m = "0"*32
        while i < 32:
            if lb[i] != hb[i]:
                break
            m = m[:i] + lb[i] + m[i+1:]
            i += 1
        for j in range(i , 32):
            if nb[j] == '0':
                if int(m[:j] + '1' + m[j+1:] , 2) <= high:
                    m = m[:j] + '1' + m[j+1:]
            else:
                if int(m[:j+1] + (32-j-1)*"1" , 2) < low:
                    m = m[:j] + '1' + m[j+1:]

        m = int(m , 2)
        print(m)

if __name__ == "__main__":
    main()
