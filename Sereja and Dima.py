n=int(input())
lst=list(map(int,input().split()))
sereja=0
dima=0
while len(lst)>0:
    if lst[0]>=lst[len(lst)-1]:
        sereja+=lst[0]
        lst.pop(0)
    elif lst[0]<=lst[len(lst)-1]:
        sereja+=lst[len(lst)-1]
        lst.pop(len(lst)-1)
    if len(lst)==0:
        continue
    if lst[0]>=lst[len(lst)-1]:
        dima+=lst[0]
        lst.pop(0)
    elif lst[0]<=lst[len(lst)-1]:
        dima+=lst[len(lst)-1]
        lst.pop(len(lst)-1)
print(sereja,dima)
