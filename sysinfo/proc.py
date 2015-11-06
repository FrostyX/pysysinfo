import psutil


def count():
    return len(psutil.pids())
