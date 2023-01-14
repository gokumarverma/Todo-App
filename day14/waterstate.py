lower = 0
upper = 100


def state(reading):
    if reading <= lower:
        return 'Solid'
    elif lower < reading < upper:
        return 'Liquid'
    else:
        return 'Gas'
