tokuten = [int(input()) for _ in range(5)]
total = 0

for i in tokuten:
    if 40 <= i:
        total += i
    else:
        total += 40

print(total // 5)
