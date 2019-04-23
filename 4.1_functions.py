import numpy as np
import matplotlib.pyplot as plt
time=np.arange(-10,10,0.01)#arrange(start,end,increment) its like for loop#
a=0
a2=0
f=100
f1=1000
amp=np.arctan(time)  #numpy has all basic signal functions inbult like sin,con, sinverse of sin(arcsin) tan #
amp1=np.arctan(time)
amp3=(1*amp1)
amp4=(1*amp)
plt.figure(1)#for separate plots of images in differnt drop boxes#
plt.subplot(221)#for more plots in single drop box subplot(r c place#
plt.plot(time,amp4)#plot(x,y) for continuous#
#plt.stem(time,amp4) for discrete plot#
plt.xlabel(f)
plt.subplot(222)
plt.plot(time,amp3)
plt.xlabel(f1)
plt.subplot(223)
plt.plot(time,(amp3+amp4))
plt.xlabel(f+f1)

plt.show()