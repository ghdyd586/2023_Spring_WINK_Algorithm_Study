a = int(input())

chk = a
for i in range(a):
    txt = input()
    for j in range(0,len(txt)-1):
        if txt[j]==txt[j+1]:
            pass
        elif txt[j] in txt[j+1:]:
            chk -=1
            break

print(chk)

