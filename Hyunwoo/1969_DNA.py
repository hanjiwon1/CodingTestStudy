N,M = map(int, input().split())
arr = []
ans = ''
total_hamming = 0

for i in range(N):
    arr.append(input())

for i in range(M):

    dic = {}
    for j in range(N):
        
        if arr[j][i] not in dic:
            dic[arr[j][i]] = 1

        else:
            dic[arr[j][i]] += 1

    dic_list = list(dic.items())
    dic_list = sorted(dic_list, key = lambda x : (-x[1], x[0]))
    
    ans += dic_list[0][0]
    total_hamming += N - dic_list[0][1]

print(ans)
print(total_hamming)