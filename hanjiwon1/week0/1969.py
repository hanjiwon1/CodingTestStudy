import sys
import string

n, m = map(int, input().split())
dna_list = []
for i in range(n):
	dna_list.append(sys.stdin.readline().replace('\n', ''))

cnt_dict = dict()
hd = 0
result = ''
for i in range(m):
	cnt_dict.update(zip([chr(i) for i in range(ord('A'), ord('Z')+1)], [0 for i in range(26)]))
	for j in range(n):
		cnt_dict[dna_list[j][i]] += 1
	max = 0
	alpha =''
	for k in range(ord('A'), ord('Z')+1):
		if max < cnt_dict[chr(k)]:
			max = cnt_dict[chr(k)]
			alpha = chr(k)
		hd += cnt_dict[chr(k)]
	result += alpha
	hd -= cnt_dict[alpha]
print(result)
print(hd)