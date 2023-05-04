nedan = list(int(input()) for _ in range(5))
print(min(nedan[:3]) + min(nedan[3:]) - 50)
