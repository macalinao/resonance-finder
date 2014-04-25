import argparse
from common import *

parser = argparse.ArgumentParser(description='Get the hertz of the sound at a given time.')
parser.add_argument('time', metavar='T', type=float, nargs='?', help='The time at which you found the resonant frequency')
args = parser.parse_args()

print freq_at_time(args.time)
