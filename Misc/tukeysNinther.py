# Tukey's ninther.
# Find a median:
#
def ninther(seq):
    seq = seq[::2]
    seq = seq[2::3]
    med = seq[len(seq)/2]
    return med

seq = ['R','L','A','P','M','C','G','A','X','Z','K','R','B','R','J','J','E']
print ninther(seq)
