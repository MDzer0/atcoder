import string
def dfs(w, d):
    if len(w) == N:
        print(w)
        return
    for i in range(d + 1):
        if i == d:
            dfs(w + wordlst[i], d + 1)
        else:
            dfs(w + wordlst[i], d)

N = int(input())
anslst = []
nlst = [0] * N
wordlst = string.ascii_lowercase
dfs('a', 1)
