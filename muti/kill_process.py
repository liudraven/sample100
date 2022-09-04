# -*- coding:UTF-8 -*-
# auther:drliu
# date:2022/9/4
# aim: 

import os
import signal
import psutil
import time
from multiprocessing import Pool
from tools.print_log import print_log


def sleep_t(i):
    time.sleep(100*i)


def start_children():
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

    pool = Pool()
    for i in range(10):
        pool.apply_async(sleep_t, (i))

    pool.close()

    _child_list = [_child.pid for _child in _p.children()]
    print_log('INFO', _child_list)
    return _child_list


def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True,
                   timeout=None, on_terminate=None):
    """Kill a process tree (including grandchildren) with signal
    "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callback function which is
    called as soon as a child terminates.
    """
    assert pid != os.getpid(), "won't kill myself"
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        try:
            p.send_signal(sig)
        except psutil.NoSuchProcess:
            pass
    gone, alive = psutil.wait_procs(children, timeout=timeout,
                                    callback=on_terminate)
    return (gone, alive)


def main():
    _child_pid_list = start_children()
    for _pid in _child_pid_list:
        kill_proc_tree(_pid)


if __name__ == '__main__':
    main()
