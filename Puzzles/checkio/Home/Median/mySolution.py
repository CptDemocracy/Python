def findAv(*args):
    return sum(args)/len(args)
    
def checkio(data):
    data.sort()
    if ( len(data) % 2 ) == 0:
        return findAv( float(data[ len(data) / 2 ]), float(data[ len(data) / 2 - 1 ]) )
    return data[ len(data) / 2 ]
