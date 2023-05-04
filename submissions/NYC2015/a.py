N = int(input())
N_2 = str(bin(N))[2:]

print("Yes" if N_2 == N_2[::-1] else "No")
