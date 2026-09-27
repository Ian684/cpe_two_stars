import sys

def main():
    his = {}
    data = sys.stdin.read()
    result = ""
    i = 0
    data += (6 - len(data)%6)*chr(0)
    while i < len(data):
        aim = ""
        b = 64
        for d in range(6):
            if ord(data[i+d]) == 0:
                continue
            if i+d == 0 or i+d == 1:
                aim += data[i+d]
                continue
            if (data[i+d-2] , data[i+d-1]) not in his:
                his[(data[i+d-2] , data[i+d-1])] = data[i+d]
                aim += data[i+d]
                continue
            if data[i+d] == his[(data[i+d-2] , data[i+d-1])]:
                b += 2**d
                continue
            else:
                his[(data[i+d-2] , data[i+d-1])] = data[i+d]
                aim += data[i+d]
                continue
        result += chr(b)
        result += aim
        i += 6
    print(result , end="")


if __name__ == "__main__":
    main()
