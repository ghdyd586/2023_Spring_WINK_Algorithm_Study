import sys
SET = [0,0,0,0,0,0,0,0,0,0,0] # 1부터 10까지 카운트 배열 생성
N = sys.stdin.readline() # 값 입력받음
LN = list(N[:-1]) # \n 제외한 나머지 값 리스트로 한글자씩 쪼갬
for i in range(len(LN)):
    if int(LN[i]) == 6 or int(LN[i]) == 9 :
        # 6혹은 9라면 -> 뒤집을 수 있음
        if SET[6] <= SET[9]:
            SET[6] +=1
        else :
            SET[9] +=1
        # 더 작은 쪽에 +1 해줌
    else :
        SET[int(LN[i])] += 1
print(max(SET))
# 가장 큰 숫자의 사용빈도를 가진 쪽 만큼 세트가 필요함

