def binary_search():

    global ans
    start, end = max(arr), sum(arr)

    while start <= end:

        mid = (start + end) // 2
        ct = 0
        have = 0

        for i in arr:

            if have < i:
                have = mid - i
                ct += 1

            else:
                have -= i
                
        if ct > M:
            start = mid + 1

        else:
            ans = mid
            end = mid - 1

N,M = map(int, input().split())
arr = []
ans = 0

for i in range(N):
    arr.append(int(input()))

binary_search()
print(ans)