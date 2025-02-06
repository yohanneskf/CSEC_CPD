n=int(input())
li=list(map(int,input().split()))
crime=0
untreated=0
police=0
for i in range(n):
    if li[i]<0:
        crime +=1
        if police > 0:
            crime -=1
            police -=1
    else:
        police +=li[i]
        untreated +=crime
        crime =0
untreated += crime
print(untreated)
