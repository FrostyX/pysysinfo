import platform


def machine():
    return platform.machine()


def hostname():
    return platform.node()


def python():
    return platform.python_version()


def system():
    return platform.system()


def distribution():
    return platform.linux_distribution()
