n=int(input())
s=input()
ant=0
dan=0
for i in range(n):
    if s[i]=="A":
        ant=ant + 1
    else:
        dan=dan + 1
if ant > dan:
    print("Anton")
elif ant < dan:
    print("Danik")
else:
    print("Friendship")
