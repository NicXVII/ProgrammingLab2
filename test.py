

a = [4, 5, 10, 12, 100]
b = a[3:5]
c = [None] * len(a)
    
for i in range(0, len(a)):
    c[len(a) - 1 - i] = a[i]


for i in range(0, len(a)):
    #print(i)
    div = a[i] / c[i]
    print(div)


a = [4, 5, 10, 12, 100]
b = a[3:5]
c = [None] * len(a)