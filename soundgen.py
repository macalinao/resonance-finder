from wavebender import *
import sys

start = 10
final = 200

end_time= 10

def val(i):
    time = float(i) / 44100
    k = (final - start) / end_time
    return math.sin(2.0 * math.pi * (start * time + ((k * time * time) / 2)))

def sweep():
    return (val(i) for i in count(0))

channels = ((sweep(),),)
samples = compute_samples(channels, 44100 * 60 * 1)
write_wavefile(sys.stdout, samples, 44100 * 60 * 1, nchannels=1)
