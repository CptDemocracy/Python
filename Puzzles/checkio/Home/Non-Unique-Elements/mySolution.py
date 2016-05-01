
# My original solution was as follows:
#
# def checkio(data):    
#     nonUniqueNumsList = []
#     for num in data:
#         if data.count(num) > 1:
#              nonUniqueNumsList.append(num)
#     return nonUniqueNumsList
#
# However as of May 1, 2016, I revised this solution
# and came up with a longer, but arguably a more
# efficient one in O(2n) (decays to O(n)) that
# requires two passes - the first pass is required
# in order to pre-calculate frequencies of data
# and the second pass to build the list of non
# unique elements.

def checkio(data):
    # pre-calculate frequencies of entries
    freqs = {}    
    for entry in data:
        if entry in freqs:
            freqs[entry] += 1
        else:
            freqs[entry] = 1

    # build a list of non unique entries
    nonUniqueList = []
    for entry in data:
        # we do not really need the "entry in freqs" check
        # but we prefer to adhere to the defensive style of
        # programming
        if entry in freqs and freqs[entry] > 1:
            nonUniqueList.append(entry)
    return nonUniqueList
