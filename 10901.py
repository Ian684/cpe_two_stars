def main():
    test = int(input())
    for _ in range(test):
        max_car , time , car = map(int , input().split())
        l = []
        r = []
        for i in range(car):
            arrive , pos = input().split()
            arrive = int(arrive)
            if pos == "left":
                l.append([arrive , i])
            else:
                r.append([arrive , i])
        l , r = sorted(l) , sorted(r)
        pos = "left"
        left , right = 0 , 0
        t = 0
        while True:
            if left >= len(l) and right >= len(r):break
            if pos == "left":
                flag = False
                for i in range(max_car):
                    if left >= len(l):break
                    if t >= l[left][0]:
                        l[left][0] = t + time
                        left += 1
                        flag = True
                if not flag:
                    if right < len(r) and t >= r[right][0]:
                        pos = "right"
                        t += time
                        continue
                else:
                    t += time
                    pos = "right"
                    continue
            else:
                flag = False
                for i in range(max_car):
                    if right >= len(r):break
                    if t >= r[right][0]:
                        r[right][0] = t + time
                        right += 1
                        flag = True
                if not flag:
                    if left < len(l) and t >= l[left][0]:
                        pos = "left"
                        t += time
                        continue
                else:
                    t += time
                    pos = "left"
                    continue
            t += 1
        left , right = 0 , 0
        l , r = sorted(l , key = lambda x : x[1]) , sorted(r , key = lambda x : x[1])
        i = 0
        while i < car:
            if left < len(l) and l[left][1] == i:
                print(l[left][0])
                left += 1
            elif right < len(r) and r[right][1] == i:
                print(r[right][0])
                right += 1
            i += 1 

        if _ != test - 1:print()

if __name__ == "__main__":
    main()
