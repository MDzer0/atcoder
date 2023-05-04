n = int(input())
low = 0
up = n + 1

while up - low > 1:
    mid = (up + low) // 2
    if ((mid + 1) * (mid)) // 2 > n + 1:
        up = mid
    else:
        low = mid

print(n + 1 - low) 
