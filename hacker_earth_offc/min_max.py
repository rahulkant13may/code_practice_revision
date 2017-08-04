inp = int(input())
if 1<=inp<=1000:
    d = input().split(' ')
    darr = [int(n) for n in d]
    if darr[0]<=darr[1]:
        mini = darr[0]
        maxi = darr[1]
    else:
        mini = darr[1]
        maxi = darr[0]
    for n in darr[2:]:
        if n<mini:
            mini = n
        elif n>maxi:
            maxi = n
    flag = 0 
    for i in range(mini, maxi):
        if i in darr:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        print('YES')
    else:
        print('NO')
    # print("min {0} and max {1}".format(mini,maxi))