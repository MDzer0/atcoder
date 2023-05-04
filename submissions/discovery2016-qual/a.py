def solve(w):
    s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
    n = len(s)
    v = [s[i:i+w] for i in range(0, n, w)]
    return "\n".join(v)

w = int(input())
print(solve(w))
