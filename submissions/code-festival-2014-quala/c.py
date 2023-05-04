A, B = map(int, input().split())

ans = B // 4 - B // 100 + B // 400
hiku = (A - 1) // 4 - (A - 1) // 100 + (A - 1) // 400

print(ans - hiku)
