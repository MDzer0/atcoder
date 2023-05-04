N = int(input())
st = []
for i in range(N):
    s, t = input().split()
    st.append([s, int(t)])
st.sort(key=lambda x: x[1], reverse=True)
print(st[1][0])
