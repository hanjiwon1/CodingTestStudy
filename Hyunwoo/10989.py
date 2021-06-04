from sys import stdin

N = int(input())
arr = [0] * 10001

for i in range(N):
    
    a = int(stdin.readline())
    arr[a] += 1

for i in range(1,10001):

    if arr[i]:
        for j in range(arr[i]):
            print(i)