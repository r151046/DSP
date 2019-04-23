import numpy as np
from matplotlib import pyplot as plt
F1=np.asarray(input("enter frequency for signal1 from 10 to 250"),'float32')
F2=np.asarray(input("enter frequency for signal2 from 10 to 250"),'float32')
Fs=np.asarray(700,'float32')
n=np.asarray(range(0,500),'float32')
x1=3*np.sin(2*np.pi*(F1/Fs)*n)
x2=np.sin(2*np.pi*(F2/Fs)*n)
#print(x1)
plt.subplot(311)
plt.plot(x1)
plt.subplot(312)
plt.plot(x2)
plt.subplot(313)
plt.plot(x1+x2)
plt.show()


