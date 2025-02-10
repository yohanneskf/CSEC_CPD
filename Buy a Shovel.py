n,r=map(int,input().split())
out=1
k=n
str_k=str(k)
while int(str_k[len(str_k)-1])!=r and int(str_k[len(str_k)-1])!=0:
    out+=1
    k=out*n
    str_k=str(k)
print(out)
