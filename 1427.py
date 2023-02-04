import sys

numbers_string = sys.stdin.readline().strip()
numbers = []
for i in range(len(numbers_string)):
    numbers.append(numbers_string[i])
numbers.sort(reverse=True)
for i in numbers:
    print(i,end='')