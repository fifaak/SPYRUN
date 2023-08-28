import psutil
import platform
from datetime import datetime
import cpuinfo
import socket
import uuid
import re
class System_information:
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    uname = platform.uname()
    system_infos = "\n"+((f"System: {uname.system}")+"\n"+
                    (f"Node Name: {uname.node}")+"\n"+
                    (f"Release: {uname.release}")+"\n"+
                    (f"Version: {uname.version}")+"\n"+
                    (f"Machine: {uname.machine}")+"\n"+
                    (f"Processor: {uname.processor}")+"\n"+
                    (f"Processor: {cpuinfo.get_cpu_info()['brand_raw']}")+"\n"+
                    (f"Ip-Address: {socket.gethostbyname(socket.gethostname())}")+"\n"+
                    (f"Mac-Address: {':'.join(re.findall('..', '%012x' % uuid.getnode()))}")+"\n"+
                    (f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"))