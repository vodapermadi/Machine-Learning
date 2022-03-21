# x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# array
x12 = []
x1x2 = []
x22 = []
x1y = []
x2y = []
y2 = []

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
for j in range(len(x1)):
    d = x1[j] ** 2
    e = x1[j] * x2[j]
    f = x2[j] ** 2
    g = x1[j] * y[j]
    h = x2[j] * y[j]
    i = y[j] ** 2
    x12 += [d]
    x1x2 += [e]
    x22 += [f]
    x1y += [g]
    x2y += [h]
    y2 += [i]

# find sigma
sX1 = sum(x1)
sX2 = sum(x2)
sX1X2 = sum(x1x2)
sX12 = sum(x12)
sX22 = sum(x22)
sX1Y = sum(x1y)
sX2Y = sum(x2y)
sY = sum(y)
sY2 = sum(y2)

# tools
n = len(x1)
a1 = n * sX1Y - (sX1) * (sY)
b1 = ((n * (sX12) - (sX1 ** 2)) * (n * (sY2) - (sY ** 2))) ** (1./2)

a2 = n * sX2Y - (sX2) * (sY)
b2 = ((n * (sX22) -(sX2 ** 2)) * (n * (sY2) - (sY ** 2))) ** (1./2)

a3 = (n * sX1X2) - (sX1 * sX2)
b3 = (((n * sX12) - (sX1 ** 2)) * ((n * sX22)-(sX2 ** 2))) ** (1./2)


r1 = a1 / b1
r2 = a2 / b2
r3 = a3 / b3

a4 = (r1 ** 2) + (r2 ** 2) - ((2 * r1 * r2 * r3))
b2 = 1 - (r3 ** 2)

r4 = (a4 / b2) ** (1./2)
# operasional


# display
print('\ndata x1 : ', x1)
print('data x2 : ', x2)
print('data x12 : ',x12)
print('data x1x2 : ',x1x2)
print('data x22 : ',x22)
print('data x1y : ',x1y)
print('data x2y : ',x2y)
print('data y : ',y)
print('data y2 : ',y2)
print('sigma x1 : ', sX1)
print('sigma x2 : ', sX2)
print('sigma y :', sY)
print('sigma y2 :', sY2)
print('sigma x1x2 : ', sX1X2)
print('sigma x12 : ', sX12)
print('sigma x22 : ', sX22)
print('sigma x1y : ', sX1Y)
print('sigma x2y : ', sX2Y)
print('data r(yx1) : ', r1)
print('data r(yx2) : ', r2)
print('data r(x1x2) : ', r3)
print('data r(yx1x2) : ', r4)
