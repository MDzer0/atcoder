n=int(input())
print('9'*n)
s='01234567899876543210'
for i in range(10**n):
  a=s[i%20]
  for j in range(1,n):
    a=s[(i//(10**j))%20]+a
  print(a)
