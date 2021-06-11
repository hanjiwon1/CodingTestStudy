import sys
n, m = map(int, input().split())
days = [int(sys.stdin.readline()) for _ in range(n)]

low, high = max(days), sum(days)
k = sum(days)

while (low <= high):
	mid = (low + high) // 2
	m_cnt = 1
	k_temp = mid
	for i in days:
		if (i <= k_temp):
			k_temp -= i
		else:
			m_cnt += 1
			k_temp = mid
			k_temp -= i

	if m_cnt > m:
		low = mid + 1
	else:
		high = mid - 1
		if k > mid:
			k = mid

print(k)