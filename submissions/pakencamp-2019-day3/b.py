N = int(input())
s = [input() for _ in range(N)]
b = s.count('black')
w = s.count('white')
if b > w:
    print('black')
else:
    print('white')
