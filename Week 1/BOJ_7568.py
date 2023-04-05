N = int(input())
List = []

for i in range(N):
    w,h = input().split()
    List.append((w,h))

for i in List:
    grade = 1
    for j in List:
        if i[0] <j[0] and i[1] < j[1]:
            grade +=1
    print(grade, end=" ")
