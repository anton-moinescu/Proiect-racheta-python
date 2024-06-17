import math
import numpy as np
import array as arr

import matplotlib.pyplot as plt

gpam=9.81
Rpam=64*pow(10,5)
eta=1.81*pow(10,-5)
rho=1.22

def gr (y):
    return gpam*(Rpam/(Rpam+y))*(Rpam/(Rpam+y))
"""
def conditiezbor (t, y, tau):
    if (float(t)<=float(tau) & float(y)>=0.0):
        return True
    else:
        return False
"""

m0=input('Masa initiala (in care este inclusa si masa combustibilului) in kg: ')
m0=float(m0)
p=input('Procentul din masa initiala care reprezinta masa combustibilului in kg: ')
p=float(p)
tau=input ('Timpul de ardere in secunde: ')
tau=float(tau)
u=input('Viteza de ardere in m/s: ')
u=float(u)
theta=input('Unghiul de lansare in grade: ')
theta=float(theta)
v0=input('Viteza initiala in m/s: ')
v0=float(v0)
D=input('Diametrul in m: ')
D=float(D)
dt=input('Incrementul de timp: ')
dt=float(dt)
y=0
x=0
t=0
m=m0
v=v0
vx=v0*math.cos(theta*math.pi/180)
vy=v0*math.sin(theta*math.pi/180)
alpha=-6.54*eta*D
beta=-0.64*rho*D*D
q=p*m0/tau

xval=[]
yval=[]
tval=[]
mval=[]
vxval=[]
vyval=[]
vval=[]

xval.append(x)
yval.append(y)
tval.append(t)
mval.append(m)
vxval.append(vx)
vyval.append(vy)
vval.append(v)

vxmax=vx
vymax=vy

i=0

while((t<=tau) & (y>=0)):
    g=gr(y)
    dvx=dt*(alpha/m*vx+beta/m*v*vx+q*u*vx/(m*v))
    dvy=dt*(-gr(y)+alpha/m*vy+beta/m*v*vy+q*u*vy/(m*v))
    vx=vx+dvx
    vy=vy+dvy
    v=math.sqrt(vx*vx+vy*vy)
    x=x+vx*dt
    y=y+vy*dt
    t=t+dt
    m=m0-q*t
    xval.append(x)
    yval.append(y)
    tval.append(t)
    mval.append(m)
    vxval.append(vx)
    vyval.append(vy)
    vval.append(v)
    i=i+1

if ((t>tau) & (y>=0)):
    while (y>=0):
        g=gr(y)
        dvx=dt*(alpha/m*vx+beta/m*v*vx)
        dvy=dt*(-gr(y)+alpha/m*vy+beta/m*v*vy)
        vx=vx+dvx
        vy=vy+dvy
        v=math.sqrt(vx*vx+vy*vy)
        x=x+vx*dt
        y=y+vy*dt
        t=t+dt

        xval.append(x)
        yval.append(y)
        tval.append(t)
        mval.append(m)
        vxval.append(vx)
        vyval.append(vy)
        vval.append(v)
        i=i+1

vmax=v0
ymax=0



for j in range (0,i+1):
    if(yval[j]>ymax):
        ymax=yval[j]
    if(vval[j]>vmax):
        vmax=vval[j]
    if(vxval[j]>vxmax):
        vxmax=vxval[j]
    if(vyval[j]>vymax):
        vymax=vyval[j]



print(f'timpul pana la revenirea la sol este: {t} ')
print(f'distanta pe Ox parcursa este: {x}')
print(f'viteza maxima atinsa este: {vmax}')
print(f'inaltimea maxima atinsa este:{ymax}')
"""
plt.figure()
for j in range(0,i+1):
    plt.plot(xval[j],yval[j])
plt.title('Traiectoria rachetei')
plt.xlabel('x')
plt.ylabel('y')
plt.show
"""

plt.subplot(221)
plt.plot(xval,yval)
plt.title('Traiectoria rachetei')
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(222)
plt.plot(tval,yval)
plt.title('Coordonata verticala in functie de timp')
plt.xlabel('t')
plt.ylabel('y')

plt.subplot(223)
plt.plot(tval,vval)
plt.title('Modulul vitezei in functie de timp')
plt.xlabel('t')
plt.ylabel('v')

plt.subplot(224)
plt.plot(tval,mval)
plt.title('Masa in functie de timp')
plt.xlabel('t')
plt.ylabel('m')

"""
plt.figure()
plt.plot(tval,vyval)
plt.title('Viteza verticala')
plt.xlabel('t')
plt.ylabel('vy')
plt.show
"""
"""
plt.subplot(121)
plt.plot(tval,vval)
plt.title('Viteza in functie de timp')
plt.xlabel('t')
plt.ylabel('v')

plt.subplot(122)
plt.plot(tval,vyval)
plt.title('Viteza verticala in functie de timp')
plt.xlabel('t')
plt.ylabel('vy')
"""

plt.show()

