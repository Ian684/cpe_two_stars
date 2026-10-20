from collections import deque
from heapq import *

def main():
    while True:
        try:
            n = int(input())
            flag = [True , True , True]
            st = []
            q = deque([])
            hq = []
            for i in range(n):
                a , b = map(int , input().split())
                if a == 1:
                    st.append(b)
                    q.append(b)
                    heappush(hq , -b)
                else:
                    if len(st) == 0 or st.pop() != b:
                        flag[0] = False
                    if len(q) == 0 or q.popleft() != b:
                        flag[1] = False
                    if len(hq) == 0 or -heappop(hq) != b:
                        flag[2] = False
        except EOFError:break
        if sum(flag) == 1:
            if flag[0]:
                print("stack")
            elif flag[1]:
                print("queue")
            elif flag[2]:
                print("priority queue")
        elif sum(flag) > 1:
            print("not sure")
        else:
            print("impossible")

if __name__ == "__main__":
    main()
