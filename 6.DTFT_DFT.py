import numpy as np
from matplotlib import pyplot as plt
n=np.arange(-200,200,1)
fs=100.0
x=np.sin(2*np.pi*20.0/fs*n)
w=np.arange(-1.0*np.pi,np.pi,np.pi/500.0)
X=[]
for i in w:                               
    sum=0;p=0;       
    for j in n:
        sum=sum+x[p]*np.exp(-1*1j*i*j)
        p=p+1;
    X=np.append(X,sum)
X_mag=np.abs(X)
X_phase=np.angle(X)

plt.subplot(311);plt.plot(n,x);
plt.subplot(312);plt.plot(w,X_mag);
plt.subplot(313);plt.plot(w,X_phase);
plt.show()
N=input('enter number of DFT points')
k=np.arange(0,N)
n1=np.arange(0,N)

if len(x)<N:
   q=N-len(x)
   x1=np.append(x,np.zeros(q))

Xk=[]
for i in k:                               
    sum=0;       
    for j in n1:
        sum=sum+x1[j]*np.exp(-1*1j*2*np.pi*i*j/np.float(N))
    Xk=np.append(Xk,sum)
Xk_mag=np.abs(Xk)
Xk_phase=np.angle(Xk)
print len(Xk)
plt.subplot(311);plt.plot(n1,x1);
plt.subplot(312);plt.plot(k,Xk_mag);
plt.subplot(313);plt.plot(k,Xk_phase);
plt.show()
