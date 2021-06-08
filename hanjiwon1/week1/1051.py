n, m = map(int, input().split())
rect = [input() for _ in range(n)]
size = 1

for i in range(n):
	for j in range(m):
		for k in range(j + 1, m):
			if (rect[i][j] == rect[i][k] and k-j < n - i):
				if (rect[i+(k-j)][k] == rect[i][j] and rect[i+(k-j)][j] == rect[i][j]):
					if (size < k - j + 1):
						size = k - j + 1
print(size**2)