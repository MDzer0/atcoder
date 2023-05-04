import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

N, M = map(int, input().split())
A = np.array(list(map(int, input().split())))
tot = np.sum(A)

if tot > N:
	print(-1)
else:
	print(N-tot)
