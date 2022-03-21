# x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# array
x12 = []
x1x2 = []
x22 = []
x1y = []
x2y = []

# input user
a = str(input('input data x1 : '))
b = str(input('input data x2 : '))
c = str(input('input data y : '))

ca = a.split(',')
cb = b.split(',')
cc = c.split(',')

x1 = [int(a)for a in ca ]
x2 = [int(b)for b in cb ]
y = [int(c)for c in cc]

# looping
for i in range(len(x1)):
    d = x1[i] ** 2
    e = x1[i] * x2[i]
    f = x2[i] ** 2
    g = x1[i] * y[i]
    h = x2[i] * y[i]
    x12 += [d]
    x1x2 += [e]
    x22 += [f]
    x1y += [g]
    x2y += [h]

# operasional
# find sigma
sX1 = sum(x1)
sX2 = sum(x2)
sX1X2 = sum(x1x2)
sX12 = sum(x12)
sX22 = sum(x22)
sX1Y = sum(x1y)
sX2Y = sum(x2y)
sY = sum(y)

# display
print('\ndata x1 : ', x1)
print('data x2 : ', x2)
print('data x12 : ',x12)
print('data x1x2 : ',x1x2)
print('data x22 : ',x22)
print('data x1y : ',x1y)
print('data x2y : ',x2y)
print('data y : ',y)
print('sigma x1 : ', sX1)
print('sigma x2 : ', sX2)
print('sigma x1x2 : ', sX1X2)
print('sigma x12 : ', sX12)
print('sigma x22 : ', sX22)
print('sigma x1y : ', sX1Y)
print('sigma x2y : ', sX2Y)
