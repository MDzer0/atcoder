s=input()
t=input()
if s==t:
  print("same")
else:
  s=s.lower()
  t=t.lower()
  if s==t:
    print("case-insensitive")
  else:
    print("different")
