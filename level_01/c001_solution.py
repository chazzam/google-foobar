def answer(y, x):
    """Find a common percent change between two lists of doubles.

    Given two lists that have a common percent change,
    identify that common percent change and return it as an int

    Args:
        x: original values, in double
        y: updated values, in double

    Returns:
        integer representation of common percent change
    """
    if len(x) == 1:
        return int( round((x[0] - y[0])/x[0] * 100) )
    x0 = set()
    for before in x:
        x1 = set()
        for after in y:
            datum = round( (before - after)/before * 100 )
            if datum >= 0:
                x1.add(datum)
        if len(x0) > 0 and len(x1) > 0:
            x0 = x0.intersection(x1)
            if len(x0) == 1:
                return int(x0.pop())
        elif len(x1) > 0:
            x0 = x1
