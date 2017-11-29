def split(seq, num):
    return [ seq[start:start+num] for start in range(0, len(seq), num) ]

