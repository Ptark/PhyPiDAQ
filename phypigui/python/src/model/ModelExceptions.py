class NumberTooSmall(Exception):
    """Raises if a number is smaller than the minimum allowed number in this context"""
    pass


class NumberTooLarge(Exception):
    """Raises if a number is larger than the maximum allowed number in this context"""
    pass


class OutOfRange(Exception):
    """Raises if a number is out of range of this context"""
    pass


class PathDoesntExist(Exception):
    """Raises if a file or directory doesn't exist"""
    pass
