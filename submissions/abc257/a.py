import string
import math

N, X = map(int, input().split())
index = math.ceil(X / N)
print(string.ascii_uppercase[index - 1])
