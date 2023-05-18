import sys
# 규칙 : 소요시간이 적은 순서대로 줄 세우기 하면 됨
N = int(sys.stdin.readline())

T = list(map(int,sys.stdin.readline().split()))
T.sort() # 작은 수 대로 정렬해줌
total = 0 # 총 소요시간

for i in range(1,N+1):
    total += sum(T[0:i])
    # 정렬한 대로 total에 더해줌
print(total) # 출력