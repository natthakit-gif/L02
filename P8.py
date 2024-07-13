def i2n(idx, flat=False):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    flat_notes = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    ns = notes
    if flat:
        ns = flat_notes

    return ns[idx-1]

def print_scale(*args):
    k = args[0]
    flat_keys = [2, 4, 6, 9, 11]
    
    print('Diatonic notes in the key of', i2n(k, flat=True), '(', k, ')')
    
    dnotes = [i2n(v, flat=True) if k in flat_keys else i2n(v) for v in args]
    
    print(' '.join(dnotes))
    print(' '.join(map(str, args)))

def diatonic(scale_key):
    intervals = [2, 2, 1, 2, 2, 2]
    scale = [scale_key]

    current_note = scale_key
    for interval in intervals:
        current_note = (current_note + interval - 1) % 12 + 1
        scale.append(current_note)
    
    return scale

if __name__ == '__main__':
    scale_key = int(input('Enter the key [1-12]:'))
    scale_notes = diatonic(scale_key)
    print_scale(*scale_notes)
