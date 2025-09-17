import psutil

for partition in psutil.disk_partitions():
    print(f"Partition: {partition.device}, Mount point: {partition.mountpoint}")
