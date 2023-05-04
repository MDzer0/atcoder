from sys import stdin
input = stdin.readline

# ���A����Ƃ��ɁA�V���������珈���B
# ��������ǉ����āA�A�������̑傫�����X�V���Ă����B
# ���ׂ��ǉ��A�擾�̗�����O�ɍ���Ă���

N,M = map(int,input().split())

tasks = []
for _ in range(M):
  a,b,y = map(int,input().split())
  tasks.append((2*y-1,a-1,b-1)) # 0-indexed

Q = int(input())
for i in range(Q):
  v,w = map(int,input().split())
  tasks.append((2*w,v-1,i)) # 0-indexed
tasks.sort(reverse=True)

size = [1] * N # �A�������̑傫��
root = list(range(N)) # �H�邱�ƂŘA�������̔���B
height = [0] * N

def find_root(x):
  y = root[x]
  if x == y:
    return x
  root[x] = find_root(y) # ���ׂ���X�V
  return root[x]

def add_edge(a,b):
  c = find_root(a)
  d = find_root(b)
  if c == d:
    return
  if height[c] > height[d]:
    root[d] = c
    size[c] += size[d]
    height[c] = max(height[d]+1,height[c])
    return
  else:
    root[c] = d
    size[d] += size[c]
    height[d] = max(height[d],height[c]+1)
    return
  
e_cnt = 0 # �t��������edge�{���B���͂���index��edge����

answer = [0]*Q

for year,x,y in tasks:
  if year%2:
    add_edge(x,y)
  else:
    answer[y] = str(size[find_root(x)])

print('\n'.join(answer))

