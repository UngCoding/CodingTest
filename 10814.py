import sys

N = int(sys.stdin.readline())

members = []
for i in range(N):
    age, name = map(str, sys.stdin.readline().split(' '))
    age = int(age)
    members.append([i, age, name])

members.sort(key=lambda x: (x[1], x[0]))

for i in range(len(members)):
    print(members[i][1] ,members[i][2], end='')