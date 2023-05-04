from collections import deque

S = input()
A = []
deq = deque()
for i in range(len(S)) :
    A.append(S)
    S = S[1:]
A.sort()

for i in range(len(A)):
    deq.append(A[i])
    print(deq.pop())
