N = int(input())
d = list(int(input()) for _ in range(N))
sumA = sum(d)
maxA = max(d)

# �Œ��̕ӂ����v�l�̔��������ł���΁A�ŏ��l��0
# �����Ő܂�Ԃ���ꍇ�A�O�p�`����������ꍇ��0�ƂȂ邽��
if sumA > maxA * 2:
    print(sumA)
    print(0)
# �Œ��̕ӂ̒������炻��ȊO�̕ӂ̒������������l���ŏ��l
else:
    print(sumA)
    print(2 * maxA - sumA)
