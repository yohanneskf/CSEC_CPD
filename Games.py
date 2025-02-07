n=int(input())
li=[[],[]]
count=0
for i in range(n):
    h,a=map(int,input().split())
    li[0].append(h)
    li[1].append(a)
for i in range(n):
    for j in range(n):
        if li[0][i]==li[1][j]:
            count+=1
print(count)
