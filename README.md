resonance-finder
================

A tool to help you find the resonance of objects in your room. Make sure you have a subwoofer.

![Resonant Frequency](http://imgs.xkcd.com/comics/resonance.png)

## Setup

You need to install the [Wavebender][wavebender] library before doing anything.

## Usage
Playing the resonant frequency of an object is simple with these 3 steps:

1. **Find when the sweeper reaches resonance.** Run `python sweeper.py | aplay` and a stopwatch simultaneously. When you reach resonance, record the time on your stopwatch.
2. **Get the resonant frequency from this time.** Use the command `python get_frequency.py 3.4` replacing `3.4` with the number of seconds elapsed (the time you recorded on the stopwatch).
3. **Play the frequency.** Use `python play_wave.py 100.0 | aplay` where `100.0` is instead the frequency from `get_frequency.py` in Hz.

Now you can troll people by shaking their desks/room/anything!

[wavebender]: https://github.com/zacharydenton/wavebender

## License

ISC
