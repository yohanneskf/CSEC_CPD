n,h=map(int,input().split())
all=list(map(int,input().split()))
width=0
for i in range(n):
    if all[i]<=h:
        width=width + 1
    else:
        width=width + 2
print(width)
