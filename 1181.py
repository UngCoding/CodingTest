import sys

N = int(sys.stdin.readline())

words = []
for i in range(N):
    words.append(sys.stdin.readline().strip('\n'))
    
words = list(set(tuple(words)))

words.sort()
words.sort(key = len) 


for word in words:
    print(word, end='\n')