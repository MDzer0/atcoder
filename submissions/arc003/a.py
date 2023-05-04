N = int(input())
s = input()
hyoka = ['A', 'B', 'C', 'D', 'E', 'F']
anslst = [0] * 5
for i in range(N):
    if hyoka[0] == s[i]:
        anslst[0] += 4
    elif hyoka[1] == s[i]:
        anslst[1] += 3
    elif hyoka[2] == s[i]:
        anslst[2] += 2
    elif hyoka[3] == s[i]:
        anslst[3] += 1

print(sum(anslst) / N)
