from collections import deque
import sys

N = int(sys.stdin.readline())
Res = []
for i in range(N):
    Res.append(sys.stdin.readline().strip())
Del = set(Res)
Res = list(Del)
Res.sort()
Res.sort(key=len)
for i in Res:
    print(i)
             
