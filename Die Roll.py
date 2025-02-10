y,w=map(int,input().split())
A=7-max(y,w)
B=6
for i in range(1,7):
    if A%i==0 and B%i==0:
        A//=i
        B//=i
out=str(A)+"/"+str(B)
print(out)
