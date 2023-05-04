import math
N = int(input())
A = list(map(int, input().split()))
card_list = [0] * 10 ** 5
for i in A:
    card_list[i] += 1

ans = 0
for i in range(1, len(card_list) // 2):
    ans += card_list[i] * card_list[len(card_list) - i]

if card_list[50000] > 1:
    ans += math.factorial(card_list[50000]) // (math.factorial(2) * math.factorial(card_list[50000] - 2))

print(ans)
