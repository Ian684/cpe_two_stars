def main():
    n = int(input())
    for c in range(n):
        s = input()
        t = input()
        ans = 0
        his = {"01":0 , "10":0 , "?0":0 , "?1":0}
        for i in range(len(t)):
            if t[i] == s[i]:continue
            his[s[i]+t[i]] += 1
        ans += min(his["01"] , his["10"])
        his["01"] -= ans
        his["10"] -= ans
        if his["?0"] >= his["01"]:
            ans += 2*his["01"]
            his["?0"] -= his["01"]
            his["01"] = 0
        if his["?1"] >= his["10"]:
            ans += 2*his["10"]
            his["?1"] -= his["10"]
            his["10"] = 0
        ans += his["?0"] + his["?1"] + his["01"]
        if his["10"] > 0:
            ans = -1
        print(f"Case {c+1}: {ans}")

if __name__ == "__main__":
    main()
