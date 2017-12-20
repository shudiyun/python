from scipy.optimize import fsolve
import math

A1 = float(input('Enter A_x : '))
A2 = float(input('Enter A_y : '))
B1 = float(input('Enter B_x : '))
B2 = float(input('Enter B_y : '))
C1 = float(input('Enter C_x : '))
C2 = float(input('Enter C_y : '))
D1 = float(input('Enter D_x : '))
D2 = float(input('Enter D_y : '))

def f(x):

    x0 = float(x[0])
    x1 = float(x[1])
    return [A1 * x0 + B1 * x1 + C1 * (1 - x0 - x1) - D1, A2 * x0 + B2 * x1 + C2 * (1 - x0 - x1) - D2]

result = fsolve(f, [1,1])

A1_ = float(input('Enter A_x_ : '))
A2_ = float(input('Enter A_y_ : '))
B1_ = float(input('Enter B_x_ : '))
B2_ = float(input('Enter B_y_ : '))
C1_ = float(input('Enter C_x_ : '))
C2_ = float(input('Enter C_y_ : '))

D1_=A1_ * result[0] + B1_ * result[1] + C1_ * (1 - result[0] - result[1])
D2_=A2_ * result[0] + B2_ * result[1] + C2_ * (1 - result[0] - result[1])

print("New coordinates for D -> (%.2f,%.2f)"%(D1_,D2_))

cos=((B1-A1)*(B1_-A1_)+(B2-A2)*(B2_-A2_))/((math.sqrt((B1-A1)*(B1-A1)+(B2-A2)*(B2-A2))*math.sqrt((B1_-A1_)*(B1_-A1_)+(B2_-A2_)*(B2_-A2_))))

angle=math.degrees(math.acos(cos))

product=(B1-A1)*(B2_-A2_)-(B2-A2)*(B1_-A1_)

if product>0:
    rotation='anticlockwise'
elif product<0:
    rotation='clockwise'
elif product==0:
    rotation='superposition'
print('angular deviation is', angle,rotation)



