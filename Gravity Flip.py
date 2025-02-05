n=int(input())
lst=list(map(int,input().split()))
lst.sort()
out=str(lst[0])
for i in range(1,n):
    out+=" "+str(lst[i])
print(out)
