import sys

i = 0
while True:
	i += 1
	l, p, v = map(int, sys.stdin.readline().split())
	if (l == 0 and p == 0 and v == 0):
		break
	d = (v // p) * l
	d += (v % p) if l > (v % p) else l
	print(f'Case {i}: {d}')