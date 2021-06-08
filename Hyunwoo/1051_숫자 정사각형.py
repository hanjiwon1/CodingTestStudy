def find_Max(s):

    for x in range(N):
        for y in range(M):

            if x + i >= N:
                continue

            elif y + i >= M:
                continue
            
            if arr[x][y] == arr[x+i][y] and arr[x][y] == arr[x][y+i] and arr[x][y] == arr[x+i][y+i]:
                return (i+1) ** 2

    return -1


N,M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(list(map(int, input())))

s = min(N,M)

for i in range(s-1,-1,-1):
    t = find_Max(i)

    if t != -1:
        print(t)
        break