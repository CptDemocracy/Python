def count_inversion(seq):
    if not hasattr(seq, "__iter__"):
        raise TypeError("a sequence expected")
        
    seqLen = len(seq)
    count  = 0

    if seqLen <= 1:
        return count

    for i in range(seqLen):        
        for j in range(i + 1, seqLen):
            if seq[i] > seq[j]:
                count += 1    

    return count
