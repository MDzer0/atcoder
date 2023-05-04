N = int(input())

flag =0
for i in range(1,101):
  if N == i**3:
    print("YES")
    flag =1
    break
if flag ==0:
  print("NO")
