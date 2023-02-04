import sys

def GCD(n, m):
    for i in range(min(n,m),0,-1):
        if n%i == 0 and m%i == 0:
            return i


M=[]        
N = int(sys.stdin.readline())
for i in range(N):
    M.append(list((map(int, sys.stdin.readline().split(' ')))))


for n in range(N):
    max_gcd = 0
    for index_m1 in range(len(M[n])):
        for index_m2 in range(index_m1+1,len(M[n])):
            if max_gcd < GCD(M[n][index_m1], M[n][index_m2]):
               max_gcd = GCD(M[n][index_m1], M[n][index_m2])
    print(max_gcd)