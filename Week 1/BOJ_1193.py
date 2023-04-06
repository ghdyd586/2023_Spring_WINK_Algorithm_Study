X = int(input())
k=1
while X>k :
    X-=k    #입력받은 수 X에서 k만큼 빼고,
    k+=1    #k는 하나씩 늘림
# ex) X 가 20인 경우
#X   k
#20  1
#19  2
#17  3
#14  4
#10  5
#5   6 ->여기까지 수행 후 while문 중단

if k%2 == 0 :
    #짝수인 경우
    bunmo = k-X+1   #짝수인 경우 분모는 내림차순
    bunja = X   #분자는 오름차순
    print("분모는 ",bunmo)
elif k%2 != 0:
    #홀수인 경우
    bunja = k-X+1
    bunmo = X

print(bunja , "/", bunmo, sep='')

# ex) X가 20인 경우, X는 5, k는 6이 나옴
# k가 짝수 이므로 분모는 6-5+1 = 2
# 분자는 5
# 따라서 출력값은 2/5

        
