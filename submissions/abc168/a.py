N = input()
if int(N[-1]) == 2 or int(N[-1]) == 4 or \
        int(N[-1]) == 5 or int(N[-1]) == 7 or \
        int(N[-1]) == 9:
    print('hon')
elif int(N[-1]) == 0 or int(N[-1]) == 1 or \
        int(N[-1]) == 6 or int(N[-1]) == 8:
    print('pon')
else:
    print('bon')
