# strace #
## 使用方法1 ##
使用strace执行程序
例如strace python install_control.py
## 使用方法2 ##
使用strace追踪已经存在的程序
strce -p pid
### 其他参数讲解 ###
- strace -tt -T -v -f -e trace=file -o /data/log/strace.log -s 1024 -p 23489
- -tt：在每行输出的前面，显示毫秒级别的时间
- -T：显示每次系统调用所花费的时间
- -v：对于某些相关调用，把完整的环境变量，文件 stat 结构等打出来。
- -f：跟踪目标进程，以及目标进程创建的所有子进程
- -e：控制要跟踪的事件和跟踪行为，比如指定要跟踪的系统调用名称
- -o：把 strace 的输出单独写到指定的文件
- -s：当系统调用的某个参数是字符串时，最多输出指定长度的内容，默认是 32 个字节
- -p：指定要跟踪的进程 pid，要同时跟踪多个 pid，重复多次 -p 选项即可


# proc #
## 查看方式 ##
ls -al /proc/pid
## 对应参数讲解 ##
1.  /proc/pid/cmdline  包含了用于开始进程的命令  ；
2.  /proc/pid/cwd 包含了当前进程工作目录的一个链接  ；
3.  /proc/pid/environ  包含了可用进程环境变量的列表  ；
4.  /proc/pid/exe  包含了正在进程中运行的程序链接；
5.  /proc/pid/fd/  这个目录包含了进程打开的每一个文件的链接；
6.  /proc/pid/mem  包含了进程在内存中的内容；
7.  /proc/pid/stat 包含了进程的状态信息；
8.  /proc/pid/statm  包含了进程的内存使用信息。


# gdb #
# perf  #
# ftrace   #
# systemtap #
# pstack #
