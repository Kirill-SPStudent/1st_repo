lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
ll = len(lst)
for ll in lst:
    if (ll < 30) and (ll % 3 == 0):
        print(ll)
