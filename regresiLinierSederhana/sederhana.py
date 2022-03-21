# x1 = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y1 = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# input user
xy = []
x2 = []
y2 = []
x = str(input('input data x : '))
y = str(input('input data y : '))

cx = x.split(',')
cy = y.split(',')

# casting data from string to int
x1 = [int(x) for x in cx]
y1 = [int(y) for y in cy]

# looping
for i in range (len(x1)):
    c = x1[i] * y1[i]
    xy += [c]

for j in range (len(x1)):
    d = x1[j] ** 2
    e = y1[j] ** 2
    x2 += [d]
    y2 += [e]

# operasional
# find sigma
sX1 = sum(x1)
sY1 = sum(y1)
sX2 = sum(x2)
sY2 = sum(y2)
sXy = sum(xy)
n = len(x1)

# find korelasi
r1 = (n * sXy) - (sX1 * sY1)
r2 = ((n * sX2 - (sX1 ** 2)) * (n * sY2 - (sY1 ** 2))) ** (1./2)
r = r1 / r2

# counting standart error
err = r / (0.5)

# display
print('\ndata x : ',x1)
print('data y : ',y1)
print('data x2 : ',x2)
print('data y2 : ',y2)
print('data xy : ',xy)
print('sigma x : ',sX1)
print('sigma y : ',sY1)
print('sigma x2 :', sX2)
print('sigma y2 :', sY2)
print('sigma xy :', sXy)
print('nilai r : ', r)
print('nilai standart error : ', err)

# mencari korelasi
# ((n*sXY) - (sX1 sY1)) var a
#  (sX2 - (sX1 ** 2)(sY2 - (sY1 ** 2)) ** (1./2)) var b == a / b
