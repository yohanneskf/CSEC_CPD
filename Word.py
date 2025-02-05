x=input()
y=[]
z=[]
for i in range(len(x)):
    if x[i]==x[i].upper():
        y.append(x[i])
    else:
        z.append(x[i])
new=""
if len(z)>=len(y):
    new=x.lower()
else:
    new=x.upper()
print(new)
