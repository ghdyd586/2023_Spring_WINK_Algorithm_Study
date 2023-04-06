a = int(input())

chk = a
for i in range(a):
    txt = input()
    for j in range(0,len(txt)-1):
        if txt[j]==txt[j+1]:
            # 특정 인덱스 단어와 다음 인덱스가 일치하는 경우
            # 똑같은 문자가 반복되는 경우임
            pass
        # ex) a가 4이고, txt가 happy, new, year, baby인 경우
        elif txt[j] in txt[j+1:]:
            # 특정 인덱스 문자가 다음 인덱스부터 단어 끝까지 중에 존재하는 경우
            # abbbbba 이런 경우, b는 if 구문에서 걸리지만, a는 elif구문에서 걸림
            chk -=1
            break
        # if경우가 1, elif 경우가 2, 그외가 3이라면
        # h -> a(3) -> p(3) -> p(1) -> y(3) : 그룹단어
        # n -> e(3) -> w(3) : 그룹단어
        # y -> e(3) -> a(3) -> r(3) : 그룹단어
        # b -> a(3) -> b(2) : 그룹단어 아님. chk 감소
print(chk)

