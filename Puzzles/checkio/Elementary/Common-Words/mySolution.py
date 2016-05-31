def checkio(csv_seq1, csv_seq2):
    separator = ","
    set1 = set(csv_seq1.split(separator))
    set2 = set(csv_seq2.split(separator))
    return separator.join(sorted(list(set1.intersection(set2))))
