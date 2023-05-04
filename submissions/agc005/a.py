X = input()
xlst = []
xlst.append(X[0])
for i in range(1, len(X)):
    if X[i] == 'S':
        xlst.append(X[i])
    else:
        if xlst != [] and xlst[-1] == 'T':
            xlst.append(X[i])
        elif xlst != [] and xlst[-1] == 'S':
            xlst.pop()
        else:
            xlst.append(X[i])

print(len(xlst))
