from math import *

def main():
    while True:
        line = input()
        if line == 'E':break
        a , ap , b , bp = line.split()
        ap , bp = float(ap) , float(bp)
        result = {}
        result[a] = ap
        result[b] = bp
        if 'T' not in result:
            e = 6.11 * (2.718281828**(5417.7530*((1/273.16) - (1/(result['D']+273.16)))))
            h = 0.5555 * (e - 10.0)
            result['T'] = result['H'] - h 
        elif 'D' not in result:
            h = result['H'] - result['T']
            e = (h/0.5555) + 10.0
            result['D'] = (1/(-(log(e/6.11)/5417.7530) + (1/273.16)))-273.16
        elif 'H' not in result:
            e = 6.11 * (2.718281828**(5417.7530*((1/273.16) - (1/(result['D']+273.16)))))
            h = 0.5555 * (e - 10.0)
            result['H'] = result['T'] + h
        print(f"T {result['T']:.1f} D {result['D']:.1f} H {result['H']:.1f}")

if __name__ == "__main__":
    main()
