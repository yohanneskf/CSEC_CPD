n = int(input())
li_bird = list(map(int, input().split()))
kill = int(input())
indx = []
shot = []
for i in range(kill):
    x, y = map(int, input().split())
    indx.append(x)
    shot.append(y)

for i in range(kill):
    index = indx[i] - 1
    if index >= 1:
        li_bird[index - 1] += shot[i] - 1
    if index < n - 1:
        li_bird[index + 1] += li_bird[index] - shot[i]
    li_bird[index] = 0

for bird in li_bird:
    print(bird)
