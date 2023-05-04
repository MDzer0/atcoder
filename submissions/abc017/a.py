s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
s3, e3 = map(int, input().split())

total = (s1 * 0.1 * e1) + (s2 * 0.1 * e2) + (s3 * 0.1 * e3)
print(int(total))
