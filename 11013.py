R = "A23456789TJQK"
S = "SHDC"
cache = {}

def run(a):
    if len(set(a)) != len(a):
        return False

    a = set(a)
    n = len(a)

    for x in range(13):
        ok = True
        for i in range(n):
            if (x + i) % 13 not in a:
                ok = False
                break
        if ok:
            return True

    return False

def value(a):
    a = tuple(sorted(a))

    if a in cache:
        return cache[a]

    if run(a):
        cache[a] = 100
        return 100

    for skip in range(5):
        b = []
        for i in range(5):
            if i != skip:
                b.append(a[i])

        if run(b):
            cache[a] = 10
            return 10

    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                x = [a[i], a[j], a[k]]
                y = []

                for p in range(5):
                    if p != i and p != j and p != k:
                        y.append(a[p])

                if run(x) and run(y):
                    cache[a] = 5
                    return 5

    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                if run([a[i], a[j], a[k]]):
                    cache[a] = 3
                    return 3

    pairs = []

    for i in range(5):
        for j in range(i + 1, 5):
            if run([a[i], a[j]]):
                pairs.append((i, j))

    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            a1, a2 = pairs[i]
            b1, b2 = pairs[j]

            if a1 != b1 and a1 != b2 and a2 != b1 and a2 != b2:
                cache[a] = 1
                return 1

    cache[a] = 0
    return 0

def main():
    deck = []

    for i in range(13):
        for j in range(4):
            deck.append((i, j))

    while True:
        line = input().strip()

        if line == "#":
            break

        cards = line.split()
        hand = []

        for c in cards:
            hand.append((R.index(c[0]), S.index(c[1])))

        used = set(hand)

        ranks = []
        for c in hand:
            ranks.append(c[0])

        best = (value(ranks) - 1) * 47
        ans = "Stay"

        for k in range(5):
            total = 0

            for c in deck:
                if c in used:
                    continue

                temp = []

                for i in range(5):
                    if i != k:
                        temp.append(hand[i][0])

                temp.append(c[0])

                total += value(temp)

            score = total - 94

            if score > best:
                best = score
                ans = "Exchange " + cards[k]

        print(ans)

if __name__ == "__main__":
    main()
