# regresion multiple

# input data
x1_data = str(input('input x1 : '))
x2_data = str(input('input x2 : '))
y_data  = str(input('input y  : '))

x1_pre = int(input('input x1 prediksi : '))
x2_pre = int(input('input x2 prediksi : '))

# split data with (,)
cy  = y_data.split(',')
cx1 = x1_data.split(',')
cx2 = x2_data.split(',')

# casting data from str to int
y  = [int(y_data) for y_data in cy]
x1 = [int(x1_data) for x1_data in cx1]
x2 = [int(x2_data) for x2_data in cx2]

# looping for find x1y,x2y,x1x2,x12,x22
x1y  = []
x2y  = []
x1x2 = []
x12  = []
x22  = []

for i in range (len(x1)):
	x1y.append(x1[i] *  y[i])
	x2y.append(x2[i] *  y[i])
	x1x2.append(x1[i] * x2[i])
	x12.append(x1[i] ** 2)
	x22.append(x2[i] ** 2)

# find sigma
n     = len(y)
sY    = sum(y)
sX1   = sum(x1)
sX2   = sum(x2)
sX1Y  = sum(x1y)
sX2Y  = sum(x2y)
sX1X2 = sum(x1x2)
sX12  = sum(x12)
sX22  = sum(x22)

#find matrix A
#            [  n  | sX1  |  sX2 ] | [  n  ][  sX1  ]
# matrix A = [ sX1 | sX12 | sX1X2] | [ sX1 ][  sX12 ]
#            [ sX2 | sX1X2| sX22 ] | [ sX2 ][  sX1X2]

#             [  sY  | sX1  |  sX2 ] | [  sY  ][  sX1  ]
# matrix A1 = [ sX1Y | sX12 | sX1X2] | [ sX1Y ][  sX12 ]
#             [ sX2Y | sX1X2| sX22 ] | [ sX2Y ][  sX1X2]

#             [  n  | sY   |  sX2 ] | [  n  ][  sY   ]
# matrix A2 = [ sX1 | sX1Y | sX1X2] | [ sX1 ][  sX1Y ]
#             [ sX2 | sX2Y | sX22 ] | [ sX2 ][  sX2Y ]

#             [  n  | sX1  |  sY  ] | [  n  ][  sX1  ]
# matrix A3 = [ sX1 | sX12 | sX1Y ] | [ sX1 ][  sX12 ]
#             [ sX2 | sX1X2| sX2Y ] | [ sX2 ][  sX1X2]

#            [  sY  ]
# matrix H = [ sX1Y ]
#            [ sX2Y ]

det_a  = ((n * sX12 * sX22) + (sX1 * sX1X2 * sX2) + (sX2 * sX1 * sX1X2) - (sX2 * sX12 * sX2) - (n * (sX1X2 ** 2)) - ((sX1 ** 2) * sX22))
det_a1 = ((sY * sX12 * sX22) + (sX1 * sX1X2 * sX2Y) + (sX2 * sX1Y * sX1X2) - (sX2 * sX12 * sX2Y) - (sY * (sX1X2 ** 2)) - (sX1 * sX1Y * sX22))
det_a2 = ((n * sX1Y * sX22) + (sY * sX1X2 * sX2) + (sX2 * sX1 * sX2Y) - (sX2 * sX1Y * sX2) - (n * sX1X2 * sX2Y) - (sY * sX1 * sX22))
det_a3 = ((n * sX12 * sX2Y) + (sX1 * sX1Y * sX2) + (sY * sX1 * sX1X2) - (sY * sX12 * sX2) - (n * sX1Y * sX1X2) - ((sX1 ** 2) * sX2Y))

# find b
b1 = det_a1 / det_a
b2 = det_a2 / det_a
b3 = det_a3 / det_a

# regresion multiple
find_y = b1 + (b2 * x1_pre) + (b3 * x2_pre)

# deploy
print(find_y)