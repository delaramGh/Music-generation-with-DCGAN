import scipy.io.wavfile as wav
import os

'''
-----------
 HOW TO USE
-----------
1. put dataSet.py in a folder
2. creat a folder named "data" where the dataSet.py is
3. put all the .wav tracks in data
4. creat a folder named "samples" in data
5. run and fun! :)
6. make sure samples folder is empty before running the program
----------
----------
the function that does the work is allTracks().
there are 2 input arguments for it. 
first one (h) tells about samples starting point fasele!
second one (t) tells about samples duration.
default values are h=5 and t=10.
-example: 
    allTracks(3, 10) will create sampels from the main track such that,
    the first sample starts from 0 to 10
    second sample starts from 3 to 13
    third one starts from 6 to 16 and so on..!
'''

def oneTrack(filename, track, h=5, t=10): #h: hampushani, t: samples duration 
    sample_rate, data = wav.read(filename)
    duration = data.shape[0] // sample_rate
    data = data[:, 0]
    print(filename, " - duration: ", duration)
    l = [i*h*sample_rate for i in range(duration//h)]
    samples = []
    for i in l:
        samples.append(data[i:i+(t*sample_rate)])
    for i in range(len(l)-5):
        wav.write(f'samples\\sample_{track}_{i}.wav', sample_rate, samples[i])

def allTracks(h=5, t=10):
    os.chdir("data")
    tracks = os.listdir()
    tracks.pop()
    i = 1
    for name in tracks:
        oneTrack(name, i, h, t)
        i += 1


if __name__ == "__main__":
    allTracks(3, 8)
