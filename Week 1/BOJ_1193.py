X = int(input())
k=1
while X>k :
    X-=k
    k+=1

if k%2 == 0 :
    #짝수인 경우
    bunmo = k-X+1
    bunja = X
    print("분모는 ",bunmo)
elif k%2 != 0:
    #홀수인 경우
    bunja = k-X+1
    bunmo = X

print(bunja , "/", bunmo, sep='')



        
