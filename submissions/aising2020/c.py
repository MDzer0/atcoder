N = int(input())
cnt = 0
anslst = [0] * (N + 1)
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            ans = i ** 2 + j ** 2 + k ** 2
            ans += i * j + j * k + k * i
            if N >= ans:
                anslst[ans] += 1

for i in anslst[1:]:
    print(i)
