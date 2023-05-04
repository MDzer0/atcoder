from collections import deque
S = input()
d = deque()

for i in range(len(S)):
    if S[i] == '(':
        d.append(i + 1)
    else:
        print(d.pop(), i + 1)
