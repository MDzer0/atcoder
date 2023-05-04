lst = list(int(input()) for _ in range(4))
m, d = divmod(sum(lst), 60)
print(m)
print(d)
