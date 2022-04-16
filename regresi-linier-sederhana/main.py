def korelasi(n,sX,sX2,sY,sY2,sXY):
    r = ((n * sXY) - (sX * sY)) / ((n * sX2 - (sX ** 2)) * (n * sY2 - (sY ** 2))) ** (1./2)
    print('\nnilai r          : ', r)

def findY(n,sX,sY,sXY,sX2,inputUser):
    b = ((n * sXY) - (sX * sY)) / (n * sX2 - (sX ** 2))
    a = (sY - b * sX) / n
    print('nilai y prediksi : ', a + b * inputUser)

# memasukan input menjadi str
x = str(input('masukan nilai x : '))
y = str(input('masukan nilai y : '))
xUser = float(input('x prediksi : '))

# memisahkan data dengan menggunakan koma
cx = x.split(',')
cy = y.split(',')

# memasukan hasil split dan mengubah type data string ke integer
x1 = [int(x) for x in cx]
y1 = [int(y) for y in cy]

# looping untuk menjumlahkan isi setiap element array
x2 = []
y2 = []
xy = []

for i in range (len(x1)):
    x2 += [x1[i] ** 2]
    y2 += [y1[i] ** 2]
    xy += [x1[i] * y1[i]]

# s adalah kepanjangan dari sigma dan n adalah banyk data dalam suatu array
n   = len(x1)
sX  = sum(x1)
sY  = sum(y1)
sX2 = sum(x2)
sY2 = sum(y2)
sXY = sum(xy)

# eksekusi kode dengan memanggil fuction
korelasi(n,sX,sX2,sY,sY2,sXY)
findY(n,sX,sY,sXY,sX2,xUser)
