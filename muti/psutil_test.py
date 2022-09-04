# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/9/4
# aim:
import time
import psutil

from tools.print_log import print_log
from multiprocessing.dummy import Pool
def useful():
    print(psutil.virtual_memory())
    print(psutil.cpu_count())
    print(psutil.disk_usage('C:\\'))
    print(psutil.net_if_addrs())
    print(psutil.pid_exists(11))

    _p = psutil.Process()
    print_log('INFO', _p.rlimit(psutil.RLIMIT_MEMLOCK))
    print_log('INFO', _p.cpu_affinity())
    print(psutil.ZombieProcess(4))
    print_log('INFO', _p.children())


def sleep_t(i):
    time.sleep(100*i)


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
    # print(psutil.pid_exists(11))
    # print(psutil.pids())
    #print(psutil.ZombieProcess(4))

    print('-----hha--------')
    _p = psutil.Process()
    print_log('INFO', _p.cpu_percent())
    print_log('INFO', _p.cpu_percent())
    print_log('INFO', _p.nice())
    print_log('INFO', _p.cpu_affinity())

    pool = Pool()
    for i in range(10):
        pool.apply_async(sleep_t, (i))

    pool.close()

    print_log('INFO', _p.children())




if __name__ == '__main__':
    main()
