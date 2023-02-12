import sys

global num
num = []

def merge_sort(A, p, r):
    if(p == r):
        return [A[p]]    
    if(p<r):
        q = (p + r) // 2
        left = merge_sort(A, p , q)
        right = merge_sort(A, q+1, r)
        return merge(left, right)
        
        
def merge(left, right):
    global num
    i, j= 0, 0
    tmp = []
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            tmp.append(left[i])
            num.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            num.append(right[j])
            j += 1
    while(i < len(left)):
        tmp.append(left[i])
        num.append(left[i])
        i += 1
    while(j < len(right)):
        tmp.append(right[j])
        num.append(right[j])
        j += 1
        
    return tmp
            
N, K = map(int, sys.stdin.readline().split(' '))
A = list(map(int, sys.stdin.readline().split(' ')))


A=merge_sort(A,0,len(A)-1)
if(K <= len(num)):
    print(num[K-1])
else:
    print(-1)