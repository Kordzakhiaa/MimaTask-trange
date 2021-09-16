'''
Write a generator trange, which generates a sequence of time tuples from start to stop incremented by step.
A time tuple is a 3-tuple of integers: (hours, minutes, seconds) 
So a call to trange might look like this:trange((10, 10, 10), (13, 50, 15), (0, 15, 12))
'''


def trange(*args):
    start = args[0]  # hour
    stop = args[1]  # minute
    step = args[2]  # second

    start_val = list(start)

    while start_val < list(stop):
        yield tuple(start_val)

        seconds = start_val[2] + step[2]
        min_rem = 0
        hour_rem = 0

        if seconds > 60:
            start_val[2] = seconds - 60
            min_rem = 1
        else:
            start_val[2] = seconds
        
        minutes = start_val[1] + step[1] + min_rem
        
        if minutes > 60:
            start_val[1] = minutes - 60
            hour_rem = 1
        else:
            start_val[1] = minutes

        hours = start_val[0] + step[0] + hour_rem

        if hours > 24:
            start_val[0] = hours - 24
        else:
            start_val[0] = hours
