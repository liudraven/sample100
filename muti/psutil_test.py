# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/9/4
# aim:
import time

import psutil

def useful():
    print(psutil.virtual_memory())
    print(psutil.cpu_count())
    print(psutil.disk_usage('C:\\'))
    print(psutil.net_if_addrs())
    print(psutil.pid_exists(11))

def main():
    # print(psutil.cpu_count())
    # print(psutil.cpu_times())
    # print(psutil.cpu_times_percent())
    # time.sleep(3)
    # print(psutil.cpu_times_percent())
    # time.sleep(3)
    # print(psutil.cpu_times_percent())
    # print('---------------')
    # print(psutil.cpu_count())
    # print(psutil.cpu_stats())
    # print(psutil.getloadavg())
    # print(psutil.virtual_memory())
    # print(psutil.disk_partitions())
    # print(psutil.disk_usage('C:\\'))
    # print(psutil.net_io_counters())
    #print(psutil.net_if_addrs())
    print(psutil.pid_exists(11))
    print(psutil.pids())
    #print(psutil.ZombieProcess(4))

if __name__ == '__main__':
    main()
