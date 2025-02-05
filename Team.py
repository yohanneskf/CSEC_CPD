n=int(input())
lst=[]
problem=0
for i in range(n):
    lst.append(list(map(int,input().split())))
for i in range(n):
    if lst[i][0]+lst[i][1]+lst[i][2]>=2:
        problem+=1
print(problem)
