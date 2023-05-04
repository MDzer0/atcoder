list1 = [int(input()), int(input()), int(input())]
list2 = sorted(list1, reverse=True)

for i in list1:
    print(list2.index(i) + 1)
