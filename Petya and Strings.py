x=input().lower()
y=input().lower()
point=0
for i in range(len(x)):
    if x[i]<y[i]:
        point=-1
        break
    elif x[i]>y[i]:
        point=1
        break
    else:
        point=0
print(point)
