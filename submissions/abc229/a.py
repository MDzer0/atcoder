S1 = input()
S2 = input()
cnt = S1.count("#")
cnt += S2.count("#")
if cnt >= 3:
    print('Yes')
else:
    if (S1[0] == "#" and S1[1] == "#") or \
            (S1[0] == "#" and S2[0] == "#") or \
            (S1[1] == "#" and S2[1] == "#") or \
            (S2[0] == "#" and S2[1] == "#"):
        print('Yes')
    else:
        print('No')
