import numpy as np 
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
from PIL import Image

def saveAudio(x, fs=44100, name='a.wav'):
    wavfile.write(name, fs, x)

def loadAudio(name):
    '''
        If the audio has 2 channels, it averages them to have a single-channel audio array.
    '''
    fs, x = wavfile.read(name)
    if len(x.shape)==2:
        x = np.average(x, -1).astype(np.int16)
    return fs, x

def transform(x, fs, nperseg=512, name=None, show=False):
    '''
        To get stft of a single-channel audio signal.
        x:  1-d numpy array
        name: name to save figure and npy files. No need to have extension.
        show: if True, it displays the stft with a figure!
    '''
    f, t, Zxx = signal.stft(x, fs=fs, nperseg=nperseg)
    if name:
        plt.imsave(name+'.png', np.abs(Zxx))
        np.save(name, np.abs(Zxx))
    if show:
        plt.figure()
        plt.imshow(np.abs(Zxx))
        plt.show()
    return np.abs(Zxx)

def itransform(z, fs):
    return signal.istft(z, fs)[1].astype(np.int16)

if __name__=='__main__':
    ##  Loading an audio...
    fs, x = loadAudio('a.wav')
    ##  Applying STFT transformation...
    Zxx = transform(x, fs, name='a', show=True)
    ##  Applying inverse STFT transformation...
    xrec = itransform(Zxx, fs)
    ##  Saving the recovered audio...
    saveAudio(xrec, name='b.wav')
    ##  Loading the saved STFT and recovering audio from it...
    img = np.load('a.npy')
    xrec1 = itransform(img, fs)
    saveAudio(xrec1, name='c.wav')