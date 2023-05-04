N = int(input())
print(0, flush=True)
l = input()
if l == 'Vacant':
    exit()
print(N - 1, flush=True)
t = input()
if t == 'Vacant':
    exit()

top = N - 1
lo = 0
while top - lo > 1:
    mid = (top + lo) // 2
    print(mid, flush=True)
    tmp = input()
    if tmp == 'Vacant':
        exit()
    elif ((mid - lo) % 2 != 0 and l == tmp) or ((mid - lo) % 2 == 0 and l != tmp):
        top = mid
    else:
        lo = mid
        l = tmp
