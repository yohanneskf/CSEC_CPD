s=input()
count=0
j=97
for i in s:
    if abs(ord(i)-j)<14:
        count+=abs(ord(i)-j)
        j=ord(i)
    else:
        count+=26- abs(ord(i)-j)
        j=ord(i)
print(count)
