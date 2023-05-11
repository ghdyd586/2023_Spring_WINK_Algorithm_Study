from collections import deque
import sys

MidofImportant = 5
printerDeq = deque()

N = int(sys.stdin.readline())
for i in range(N):
    C,M = map(int,sys.stdin.readline().split())
    
    list = [map(int,sys.stdin.readline())]

    for t in list:
        printerDeq.append(t)
    
    getMax = max(printerDeq)

    while 1 :
        tmp = printerDeq.popleft()
        if printerDeq.count == 0 :
            print(1)
            break
        cnt = 1
        if tmp == getMax :
            
            getmax = max(printerDeq)
            M -=1
            cnt+=1
        else:
            printerDeq.append(tmp)
        if M == 0:
            print(cnt)

