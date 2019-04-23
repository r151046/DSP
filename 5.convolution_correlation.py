import numpy as np
from matplotlib import pyplot as plt
def convolute(x,h):
    lx=len(x)
    lh=len(h)
    y=[]
    for n in range(lx+lh-1):
        sum=0
        for k in range(lx):
            if n-k<lh and n-k>=0:
                sum=sum+x[k]*h[n-k]
        y=np.append(y,sum)
    return y

def time_rev(x):
    lx=len(x)
    y=[]
    for i in range(0,lx):
	y=np.append(y,x[lx-i-1])
    return y
'''
x=np.array(input('enter seq1'))
h=np.array(input('enter seq2'))
print(convolute(x,h))
print('conv=',np.convolve(x,h))
print(convolute(x,time_rev(h)))
'''
n=np.arange(0,500)
x=np.sin(2*np.pi*20.0/400.0*n)
N=np.sin(2*np.pi*50.0/400.0*n)
N1=np.random.rand(x.shape[0])
x_N=x+N+N1
h=[1.0/3.0,1.0/3.0,1.0/3.0]
y1=convolute(h,x_N)
y2=convolute(x+N,time_rev(x+N)) #autocorrelation of x
y3=convolute(x_N,time_rev(x_N)) #autocorrelation of X_N
#print(y1,y2)
a1=plt.subplot(611)
a1.plot(x+N)
a2=plt.subplot(612,sharex=a1)
a2.plot(N1)
a3=plt.subplot(613,sharex=a1)
a3.plot(x_N)
a4=plt.subplot(614,sharex=a1)
a4.plot(y1)
a4=plt.subplot(615,sharex=a1)
a4.plot(y2)
a4=plt.subplot(616,sharex=a1)
a4.plot(y3)
plt.show()

