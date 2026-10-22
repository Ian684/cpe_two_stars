def water(f , l , k , t1 , t2):
    
    if f <= l:return f
    r = f / t1
    if r <= k:return l

    t = l / r
    h = l + (t1 - t)*(r - k)

    h = max(l , h - k*t2)
    return h

def main():
    n = int(input())
    eps = 1e-9
    for _ in range(n):
        l , k , t1 , t2 , h = map(float , input().split())

        left , right = 0 , h + k*(t1+t2) + 10000
        
        while True:
            mid = (left + right) / 2
            temp = water(mid , l , k , t1 , t2)
            if right - left <= eps:
                ans1 = mid
                break
            if temp >= h:
                right = mid
            else:
                left = mid

        left , right = 0 , h + k*(t1+t2) + 10000

        while True:
            mid = (left + right) / 2
            temp = water(mid , l , k , t1 , t2)
            if right - left <= eps:
                ans2 = mid
                break
            if temp > h:
                right = mid
            else:
                left = mid
        print(f"{ans1:.6f} {ans2:.6f}")

if __name__ == "__main__":
    main()
