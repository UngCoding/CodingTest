import sys

N = int(sys.stdin.readline())

points = list(map(int, sys.stdin.readline().split(' ')))
points_set = list(set(points))
points_set.sort()
points_dict ={}
for index, point in enumerate(points_set):
    points_dict[point] = index
    
for point in points:
    print(points_dict[point], end=' ')