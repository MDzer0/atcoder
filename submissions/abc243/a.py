V,A,B,C=list(map(int,input().split()))
unit=A+B+C
remain=V%unit

if remain<A:
    print('F')
elif A<=remain and remain<A+B:
    print('M')
else:
    print('T')
