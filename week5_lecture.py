# Script arguments

import sys

name = sys.argv[1]
age = int(sys.argv[2])

print(f"My name is {name} and I am {age} years old")

# psutils 1
import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()

print(f"CPU: {cpu}%")
print(f"Memory: {memory.percent}%")

# psutils 2

print(psutil.disk_partitions())

# psutils 3

for partition in psutil.disk_partitions():
    print(partition.device)
