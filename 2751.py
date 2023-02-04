import sys

def heapify(numbers, index, heap_size):
    largest = index
    left_index = index*2 + 1
    right_index = index*2 + 2
    
    if left_index < heap_size and numbers[largest] < numbers[left_index]:
        largest = left_index
    
    if right_index < heap_size and numbers[largest] < numbers[right_index]:
        largest = right_index
    
    if largest != index:
        numbers[largest], numbers[index] = numbers[index], numbers[largest]
        heapify(numbers, largest, heap_size)
        
    


def heap_sort(numbers):
    n = len(numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, i,n)
        
    for i in range(n - 1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers,0, i)
        
    return numbers
        


N = int(input())
numbers=[]
for i in range(N):
    numbers.append(int(sys.stdin.readline()))
    
numbers = heap_sort(numbers)

for i in numbers:
    print(int(i), end = "\n")