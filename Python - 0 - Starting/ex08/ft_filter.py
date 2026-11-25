def ft_filter(function, iterable):
    """
    Construct an iterator from those elements of iterable for which
    function is true. If function is None, return the items that are true.
    """
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item