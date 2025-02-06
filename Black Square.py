a=list(map(int,input().split()))
s=input()
Sum=0
for i in s:
    Sum +=a[int(i)-1]
print(Sum)
