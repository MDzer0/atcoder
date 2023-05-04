MOD = 10 ** 9 + 7

def kurikaeshi(a, b):
    ans = 1
    p = a
    for i in range(30):
        waru = 1 << i
        if (b // waru) % 2 == 1:
            ans = (ans * p) % MOD
        p = p ** 2 % MOD
    return ans

a, b = map(int, input().split())

print(kurikaeshi(a, b))
