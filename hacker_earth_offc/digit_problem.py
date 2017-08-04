x, k = map(int, input().split())

xs = str(x)

for i in range(len(xs)-1):
    if xs[i] != '9':
        # xs[i] = '9'

        print(i, x)
        # xs[i] = '9'
list1 = list(xs)
list1[2] = '7'
xs = ''.join(list1)
xs.replace(xs[0], '5')
print(xs[0])
print(xs[1])
print(xs[2])
print(xs[3])
print(xs[4])
print(xs)