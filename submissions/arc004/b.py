N = int(input())
d = list(int(input()) for _ in range(N))
sumA = sum(d)
maxA = max(d)

# 最長の辺が合計値の半分未満であれば、最小値は0
# 半分で折り返せる場合、三角形が成立する場合に0となるため
if sumA > maxA * 2:
    print(sumA)
    print(0)
# 最長の辺の長さからそれ以外の辺の長さを引いた値が最小値
else:
    print(sumA)
    print(2 * maxA - sumA)
