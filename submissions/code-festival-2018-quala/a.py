abcs = [int(input()) for _ in range(4)]
total = sum(abcs[:3])
if total <= abcs[3] <= total + 3:
    print('Yes')
else:
    print('No')
