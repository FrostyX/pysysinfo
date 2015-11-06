#!/usr/bin/python

import sys
from pysysinfo import proc, mem, system


if __name__ != "__main__":
    sys.stderr.write('The executable of pysysinfo must not be imported.')
    sys.exit(1)


info = {
    "sys": system.system(),
    "distro": " ".join(map(str, system.distribution()[:-1])),
    "machine": system.machine(),
    "hostname": system.hostname(),
    "python": system.python(),
    "mem": mem.percent(),
    "proc": proc.count(),
}


print("""System information
==================

SYS:
----
System:   {sys}
Distro:   {distro}
Machine:  {machine}
Hostname: {hostname}
Python:   {python}

MEM:
----
Free:     {mem}

Processes:
Count:    {proc}
""".format(**info))
