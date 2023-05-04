N = int(input())
S = input()
ssort = ['J', 'O', 'I']
ans = ''
for i in ssort:
    for j in S:
        if i == j:
            ans += j

print(ans)
