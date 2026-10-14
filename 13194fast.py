import math
import random
from collections import Counter

def is_prime(n):
    if n < 2:
        return False

    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False

    return True


def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    while True:
        c = random.randrange(1, n)
        x = random.randrange(2, n)
        y = x
        d = 1

        while d == 1:
            x = (x*x + c) % n
            y = (y*y + c) % n
            y = (y*y + c) % n

            d = math.gcd(abs(x-y), n)

        if d != n:
            return d


def factor(n, result):
    if n == 1:
        return

    if is_prime(n):
        result.append(n)
        return

    d = pollard_rho(n)

    factor(d, result)
    factor(n // d, result)


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        factors = []
        factor(n, factors)

        counts = Counter(factors)

        sigma = 1

        for p, k in counts.items():
            sigma *= (p**(k+1) - 1) // (p-1)

        sigma -= n

        if sigma == n:
            print("perfect")
        elif sigma < n:
            print("deficient")
        else:
            print("abundant")


if __name__ == "__main__":
    main()
