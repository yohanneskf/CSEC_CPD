x=input()
y=[]
for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])
z=""
if len(y)%2==0:
    z="CHAT WITH HER!"
else:
    z="IGNORE HIM!"
print(z)
