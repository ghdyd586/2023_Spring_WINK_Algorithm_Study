from collections import deque
import sys

NumDeq = deque()
TmpDeq = deque()
N,M = map(int,sys.stdin.readline().split())
list = list(map(int,sys.stdin.readline().split()))
for i in list :
    TmpDeq.append(i)
cnt = 0
tmp = 0
trial = 0
for i in range(N):
    NumDeq.append(i)
while cnt <= M :
    tmp = NumDeq.pop()
    tmp2 = TmpDeq.popleft()
    for j in range(len(list)):
        if tmp == tmp2 :
            cnt+=1
        elif tmp < tmp2 :
            NumDeq.appendleft(tmp)
            TmpDeq.appendleft(tmp2)
            trial +=1
        else :
            NumDeq.append(NumDeq.popleft())
            TmpDeq.appendleft(tmp2)
            trial +=1
    
print(trial)
