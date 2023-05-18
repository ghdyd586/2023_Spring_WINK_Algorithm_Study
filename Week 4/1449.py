import sys

N,L = map(int, sys.stdin.readline().split())
need = 0
tmp = L
K = list(map(int,sys.stdin.readline().split()))

while 1 :
    if (L >= N) :
        need += 1
        break
    else :
        need += 1
        L *= 2


print(need)