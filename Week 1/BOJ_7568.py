N = int(input())
List = []

for i in range(N):
    w,h = input().split()
    List.append((w,h))

for i in range(len(List)-1):
    grade = 1
    if List[i][0] > List[i+1][0] :
        if List[i+1][1] > List[i+1][1]:
            grade += 1
    print(grade, end=" ")

# 왜 자꾸 1만 뜨는지 모르겠습니다....
