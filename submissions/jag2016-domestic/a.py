def check():
  N = int(input())
  cnt = 0
  for _ in range(N):
    s = input()
    if s=="A":
      cnt +=1
    else:
      cnt -=1
    
    if cnt<0:
      return False
    
  return cnt == 0

if __name__ == "__main__":
  if check():
    print("YES")
  else:
    print("NO")
