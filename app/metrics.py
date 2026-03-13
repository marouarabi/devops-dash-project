import os
import platform
import socket
import time
from datetime import datetime

import psutil


def get_system_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time

    metrics = {
        "cpu_percent": cpu_percent,
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "cpu_cores": psutil.cpu_count(logical=True),
        "hostname": socket.gethostname(),
        "os": f"{platform.system()} {platform.release()}",
        "current_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "uptime": str(uptime).split('.')[0]
    }

    return metrics