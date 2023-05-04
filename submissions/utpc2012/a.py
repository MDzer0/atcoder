S=list(input().split('/'))
a=S[0]
b=S[1]+S[2]
a=sorted(a)
b=sorted(b)
if a==b:
  print("yes")
else:
  print("no")
