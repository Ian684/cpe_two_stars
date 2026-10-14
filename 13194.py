def generate(n):
    n = int(n**0.5)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    return [i for i in range(2, n+1) if is_prime[i]]

def main():
    prime = generate(10**12)
    test = int(input())
    for _ in range(test):
        n = int(input())
        temp = n
        r = 1
        for p in prime:
            if p*p > temp: break
            if temp == 1:break
            if temp % p == 0:
                count = 0
                while temp % p == 0:
                    temp //= p
                    count += 1
                r *= (1-p**(count + 1))//(1-p)
        if temp > 1:
            r *= (1 + temp)
        r -= n
        if n == r:
            print("perfect")
        elif n > r:
            print("deficient")
        elif n < r:
            print("abundant")        
        
if __name__ == "__main__":
    main()
