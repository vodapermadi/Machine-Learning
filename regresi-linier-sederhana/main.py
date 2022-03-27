def korelasi(n,sX,sX2,sY,sY2,sXY):
    r1 = (n * sXY) - (sX * sY)
    r2 = ((n * sX2 - (sX ** 2)) * (n * sY2 - (sY ** 2))) ** (1./2)
    r = r1 / r2
    print('\nnilai r          : ', r)

def findY(n,sX,sY,sXY,sX2,inputUser):
    b = ((n * sXY) - (sX * sY)) / (n * sX2 - (sX ** 2))
    a = (sY - b * sX) / n
    print('nilai y prediksi : ', a + b * inputUser)

x = str(input('masukan nilai x : '))
y = str(input('masukan nilai y : '))
xUser = float(input('nilai yang di prediksi :'))

x2 = []
y2 = []
xy = []
cx = x.split(',')
cy = y.split(',')
x1 = [int(x) for x in cx]
y1 = [int(y) for y in cy]

for i in range (len(x1)):
    x2 += [x1[i] ** 2]
    y2 += [y1[i] ** 2]
    xy += [x1[i] * y1[i]]

n   = len(x1)
sX  = sum(x1)
sY  = sum(y1)
sX2 = sum(x2)
sY2 = sum(y2)
sXY = sum(xy)

korelasi(n,sX,sX2,sY,sY2,sXY)
findY(n,sX,sY,sXY,sX2,xUser)
