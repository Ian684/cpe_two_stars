from math import *

def main():
    alph = {}
    k = 1
    for i in range(26):
        alph[chr(97+i)] = k
        alph[chr(65+i)] = k+26
        k += 1
    while True:
        try:
            count = 0
            for l in input():
                count += alph[l]
            flag = True
            for i in range(2 , int(sqrt(count))+1):
                if count % i == 0:
                    flag = False
                    break
            if flag:
                print("It is a prime word.")
            else:
                print("It is not a prime word.")
        except EOFError:break

if __name__ == "__main__":
    main()
