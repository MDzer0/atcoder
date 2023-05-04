S = [input() for _ in range(4)]
m_list = ['H', '2B', '3B', 'HR']

for i in m_list:
    if not(i in S):
        print('No')
        exit()

print('Yes')
