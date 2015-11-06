import psutil


def percent():
    return psutil.virtual_memory()[2]
