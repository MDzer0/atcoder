N = int(input())
if N <= 2014 or N == 2017:
    print(-1)
elif N <= 2016:
    print(N - 2014)
else:
    print(N - 2015)
