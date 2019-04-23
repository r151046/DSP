import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
fs,data=wav.read('akon.wav')
n=data.shape[0]
x=np.exp(-1*np.arange(0,10))
