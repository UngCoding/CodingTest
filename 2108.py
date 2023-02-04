import sys

N = int(sys.stdin.readline())

numbers = []
mode_n = 0
mode_count = 0
count = 1

for i in range(N):
    numbers.append(int(sys.stdin.readline()))


print(round(sum(numbers)/N))



numbers.sort()

print(numbers[N//2])


mode = numbers[0]
for i in range(N):
    
    if numbers[i-1] == numbers[i]:
        count += 1
    elif numbers[i-1] != numbers[i]:
        count = 1
    
    if mode_n < count and mode != numbers[i]:
        mode_n = count
        mode_count = 0
        mode = numbers[i]
    elif mode_n < count and mode == numbers[i]:
        mode_n = count
        mode_count = 0
    elif mode_n == count:
        mode_count += 1
        if mode_count >= 2:
            continue
        else:
            mode = numbers[i]
print(mode)

print(max(numbers) - min(numbers))