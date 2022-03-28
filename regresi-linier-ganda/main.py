# rumus find Y
# b = ((n * sXY) - (sX * sY)) / (n * sX2 - (sX ** 2))
# a = (sY - b * sX) / n
# y = a + bX

# table penolong
# x1,x2,x12,x22,x1x2,y,y2

def findY(n,sX1Y,sX2Y,sX1,sX2,sY1,sX12,sX22,xUser,xUser2):
    b1 = ((n * sX1Y) - (sX1 * sY1)) / (n * sX12 - (sX1 ** 2))
    b2 = ((n * sX2Y) - (sX2 * sY2)) / (n * sX22 - (sX2 ** 2))
    a = ((sY1 / n ) - (b1 * (sX1 / n)) - (b2 * (sX2 / n)))
    y = a + (b1 * xUser) + (b2 * xUser2)
    print('data Y adalah: ')

x = str(input('masukan nilai x1 : '))
xx = str(input('masukan nilai x2 : '))
y = str(input('masukan nilai y : '))
user1 = int(input('data pre var 1 :'))
user2= int(input('data pre var 2 :'))

kx = x.split(',')
kxx = xx.split(',')
ky = y.split(',')

x1 = [int(x)for x in kx]
x2 = [int(xx)for xx in kxx]
y1 = [int(y)for y in ky]

x12 = []
x22 = []
x1x2 = []
x1y = []
x2y = []
y2 = []

for i in range(len(x1)):
    x12 += [x1[i] ** 2]
    x22 += [x2[i] ** 2]
    x1x2 += [x1[i] * x2[i]]
    x1y += [x1[i] * y1[i]]
    x1y += [x2[i] * y1[i]]
    y2 += [y1[i] ** 2]

# sigma
n = sum(x1)
sX1 = sum(x1)
sX12 = sum(x12)
sX2 = sum(x2)
sX22 = sum(x22)
sX1X2 = sum(x1x2)
sX1Y = sum(x1y)
sX2Y = sum(x2y)
sY1 = sum(y1)
sY2 = sum(y2)

findY(n,sX1Y,sX2Y,sX1,sX2,sY1,sX12,sX22,user1,user2)
