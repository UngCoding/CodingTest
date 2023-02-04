import sys

N = int(sys.stdin.readline())
points = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split(' '))
    points.append([x,y])

points.sort()

for i in range(len(points)):
        print(points[i][0], points[i][1], end='\n')