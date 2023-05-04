from sys import stdin
input = stdin.readline

# 道、質問ともに、新しい道から処理。
# 順次道を追加して、連結成分の大きさを更新していく。
# やるべき追加、取得の列を事前に作っておく

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

size = [1] * N # 連結成分の大きさ
root = list(range(N)) # 辿ることで連結成分の判定。
height = [0] * N

def find_root(x):
  y = root[x]
  if x == y:
    return x
  root[x] = find_root(y) # 調べたら更新
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
  
e_cnt = 0 # 付け加えたedge本数。次はそのindexのedgeから

answer = [0]*Q

for year,x,y in tasks:
  if year%2:
    add_edge(x,y)
  else:
    answer[y] = str(size[find_root(x)])

print('\n'.join(answer))

