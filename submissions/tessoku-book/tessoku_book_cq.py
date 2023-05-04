import sys

# ����
N, S = map(int, input().split())
A = list(map(int, input().split()))

# ���I�v��@�ii=0�j
dp = [ [ None ] * (S + 1) for i in range(N + 1) ]
dp[0][0] = True
for i in range(1, S+1):
	dp[0][i] = False

# ���I�v��@�ii=1�j
for i in range(1, N+1):
	for j in range(0,S+1):
		if j < A[i-1]:
			if dp[i-1][j] == True:
				dp[i][j] = True
			else:
				dp[i][j] = False

		if j >= A[i-1]:
			if dp[i-1][j] == True or dp[i-1][j-A[i-1]] == True:
				dp[i][j] = True
			else:
				dp[i][j] = False

# �I�ѕ������݂��Ȃ��ꍇ
if dp[N][S] == False:
	print("-1")
	sys.exit(0)

# �����̕���
Answer = []
Place = S
for i in reversed(range(1,N+1)):
	if dp[i-1][Place] == True:
		Place = Place - 0 # �J�[�h i ��I�΂Ȃ�
	else:
		Place = Place - A[i-1] # �J�[�h i ��I��
		Answer.append(i)
Answer.reverse()

# �������o��
Answer2 = [str(i) for i in Answer]
print(len(Answer))
print(" ".join(Answer2))
