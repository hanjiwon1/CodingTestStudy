import sys
N = int(input())

cnt_num = [0 for _ in range(10001)]
for i in range(N):
	cnt_num[int(sys.stdin.readline())] += 1

cnt = 0
i = 0
while True:
	if (cnt_num[i] != 0):
		for _ in range(cnt_num[i]):
			sys.stdout.write(str(i)+'\n')
			cnt += 1
	if (cnt == N):
		break
	i += 1

