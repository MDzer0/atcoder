N = int(input())
ans1 = 'nO'
ans2 = 'nO'
if N % 6 == 0:
    ans1 = 'yES'
if N % 11 == 0:
    ans2 = 'yES'
print(ans1)
print(ans2)
