X = input()
ans = 'YES'
index = 0
while True:
    if X[index] == 'o' or X[index] == 'k' or X[index] == 'u':
        index += 1
    elif X[index: index + 2] == 'ch':
        index += 2
    else:
        ans = 'NO'
        break

    if index == len(X):
        break

print(ans)
