K = int(input())
d, m = divmod(K, 60)
print(str(21 + d) + ':' + str(m).zfill(2))
