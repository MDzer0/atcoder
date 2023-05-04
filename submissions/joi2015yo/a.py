A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
if P <= C:
    print(min(P * A, B))
else:
    print(min(P * A, B + (P - C) * D))
