sx, sy, tx, ty = map(int, input().split())
xtmp = abs(sx - tx)
ytmp = abs(sy - ty)
ans = 'U' * ytmp
ans += 'R' * xtmp
tmp1 = ans
tmp1 = tmp1.replace('R', 'L')
tmp1 = tmp1.replace('U', 'D')
tmp2 = 'LU' + ans + 'RD'
tmp3 = 'RD' + tmp1 + 'LU'
print(ans + tmp1 + tmp2 + tmp3)
