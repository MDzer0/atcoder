S = input()
alst = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Si']
cnt = 0
for i in range(1, 20):
    if S[i - 1] == S[i] and S[i + 6] == S[i + 7]:
        cnt = i
        break

if 2 <= cnt <= 3:
    print(alst[1])
elif 4 <= cnt <= 5:
    print(alst[0])
elif 6 == cnt:
    print(alst[6])
elif 7 <= cnt <= 8:
    print(alst[5])
elif 9 <= cnt <= 10:
    print(alst[4])
elif 11 <= cnt <= 12:
    print(alst[3])
else:
    print(alst[2])
