A, op, B = map(str, input().split())
ans = 0
if op == '+':
    ans = int(A) + int(B)
else:
    ans = int(A) - int(B)
    
print(ans)
