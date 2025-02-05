n=int(input())
x=[]
num=[]
j=1
for i in range(n):
    x.append(input())
while j<n:
    if x[j-1]!=x[j]:
        num.append("1")
    j+=1
print(len(num)+1)
