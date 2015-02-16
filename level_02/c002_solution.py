# Hah, realized after I submitted this that it doesn't actually handle the problem correctly
# It only reduces splits across one range, if splits are reducable in another range it won't necessarily find them
# So this needs to be redone, but not now...
def reduce_splits(times):
    earliest = times[0][0]
    latest = times[0][1]
    if len(times) == 1:
        return latest - earliest
    splits = []
    # reduce our input, build splits if needed
    while len(times) > 0:
        x = times.pop()
        if x[0] >= earliest and x[1] <= latest:
            continue
        if x[0] < earliest and x[1] > latest:
            # extend in both directions
            earliest = x[0]
            latest = x[1]
        elif x[0] < earliest and x[1] >= earliest:
            # Lower the lower bound
            earliest = x[0]
        elif x[0] <= latest and x[1] > latest:
            # raise the upper bound
            latest = x[1]
        elif x not in splits:
            # Save for later
            splits.append(x)
    if len(splits) == 0:
        return latest - earliest
    else:
        # rebuild our input
        times.append([earliest, latest])
        times.extend(splits)
        return -1

def answer(intervals):
    # Reduce the number of intervals to find the time
    time_length = reduce_splits(intervals)
    if time_length > 0:
        return time_length
    # Check for resolvable splits in the time
    num_splits_before = len(intervals)
    num_splits_after = 0
    while num_splits_before != num_splits_after:
        num_splits_before = len(intervals)
        time_length = reduce_splits(intervals)
        num_splits_after = len(intervals)
        if time_length > 0:
            return time_length
    # Get the total time across splits
    time_length = 0
    for x in intervals:
        time_length += x[1] - x[0]
    return time_length
