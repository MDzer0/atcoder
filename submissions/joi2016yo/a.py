tokuten = [int(input()) for _ in range(6)]
tmp1 = sorted(tokuten[:4], reverse=True)
tmp2 = sorted(tokuten[4:], reverse=True)
print(sum(tmp1[:3]) + tmp2[0])
