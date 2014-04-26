from wavebender import *
import sys
from common import *

def sweep():
    return (val(i) for i in count(0))

channels = ((sweep(),),)
samples = compute_samples(channels, 44100 * 60 * 1)
write_wavefile(sys.stdout, samples, 44100 * 60 * 1, nchannels=1)
