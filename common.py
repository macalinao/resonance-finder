start = 10
final = 200

end_time = 10
k = (final - start) / end_time

def val_at_time(time):
    return math.sin(2.0 * math.pi * (start * time + ((k * time * time) / 2)))

def freq_at_time(time):
    return start + k * time

def val(i):
    time = float(i) / 44100
    return val_at_time(time)
