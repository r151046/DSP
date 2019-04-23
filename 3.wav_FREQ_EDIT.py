import scipy.io.wavfile as wav
from matplotlib import pyplot as plt
import numpy as np
fs,data=wav.read('akon.wav')#file man.wav in terminal shows about the file#
print(fs)
print(data)
##fsx=np.array([fs])
#datay=np.array([data])
#plt.plot(fsx,datay)##

wav.write('akon1.5f.wav',(1.5)*fs,data)
