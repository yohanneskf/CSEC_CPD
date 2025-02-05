met=[[],[],[],[],[]]
for i in range(5):
    met[i]=list(map(int,input().rstrip().split()))
index_1=[]
for i in range(5):
    for j in range(5):
        if met[i][j]==1:
            index_1=[i,j]
ansr=abs(index_1[0]-2)+abs(index_1[1]-2)
print(ansr)
