def digital_root(n):
    # ...
    sums=sum([int(x) for x in list(str(n))])
    if sums<10:
        return sums
    else:
        return digital_root(sums)