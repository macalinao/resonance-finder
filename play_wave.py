from wavebender import *
import sys
from common import *

parser = argparse.ArgumentParser(description='Play a sine wave at a given frequency.')
parser.add_argument('freq', metavar='F', type=float, nargs='?', help='The resonant frequency')
args = parser.parse_args()

wave = sine_wave(args.freq, 44100, 1)

channels = ((wave,),)
samples = compute_samples(channels, 44100 * 60 * 1)
write_wavefile(sys.stdout, samples, 44100 * 60 * 1, nchannels=1)
