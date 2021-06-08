ct = 1

while True:
    
    L,P,V = map(int, input().split())
    
    if L == 0 and P == 0 and V == 0:
        break
    
    ans = L * (V // P)
    
    if V % P <= L:
        ans += V % P

    else:
        ans += L

    a = f'Case {ct}: {ans}'
    print(a)
    
    ct += 1