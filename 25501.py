import sys

global cnt 
cnt = 1

def recursion(s, l, r):
    global cnt 
    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else:
        cnt += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(sys.stdin.readline())

words = []
for i in range(T):
    words.append(sys.stdin.readline().strip('\n'))
    
for i in range(T):
    print(isPalindrome(words[i]), cnt)
    cnt = 1
