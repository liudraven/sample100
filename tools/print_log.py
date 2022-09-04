# -*- coding:utf-8 -*-

import os
import time
import traceback
import logging
from logging.handlers import TimedRotatingFileHandler

__all__ = ['print_log']
cur_file = os.path.abspath(__file__)
cur_path = os.path.dirname(cur_file)

# 建议配置项
# 日志名称
global_log_file = cur_file + '.log'
# 错误日志名称
global_error_log_file = cur_file + '_error.log'
# 日志级别
global_log_level = logging.DEBUG
#global_log_level = logging.INFO


# python logging
class Py_Logger(object):
    log_level = global_log_level
    log_file = global_log_file
    error_log_file = global_error_log_file

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        log_dir = os.path.join(cur_path, '../log')

        log_path = os.path.join(log_dir, self.log_file)
        self.error_log_path = os.path.join(log_dir, self.error_log_file)
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        # 清空当前文件的logging
        logging.Logger.manager.loggerDict.pop(__name__, None)
        self.logger.handlers = []
        self.logger.removeHandler(self.logger.handlers)

        if not self.logger.handlers:
            # logger 配置等级
            self.logger.setLevel(global_log_level)
            # file handler
            self.fh = TimedRotatingFileHandler(log_path, when='MIDNIGHT', interval=1, backupCount=3)
            self.fh.setLevel(global_log_level)

            # console handler
            self.ch = logging.StreamHandler()
            self.ch.setLevel(global_log_level)

            # set format for handlers
            f_format = "%(asctime)s [%(levelname)s] %(message)s"
            formatter = logging.Formatter(f_format)
            self.fh.setFormatter(formatter)
            self.ch.setFormatter(formatter)

            # 添加handler
            # self.logger.addHandler(self.fh)
            console_flag = self.get_console_flag()
            if console_flag:
                self.logger.addHandler(self.ch)

    # 获取console_flag
    def get_console_flag(self):
        console_flag = True
        console_flag_file = os.path.join(cur_path, 'console_flag.txt')
        if os.path.isfile(console_flag_file):
            with open(console_flag_file, 'r') as f:
                console_flag = False if f.read().strip() == '0' else True
        return console_flag

    def info(self, message=None):
        self.__init__()

        self.logger.info(message)

    def debug(self, message=None):
        self.__init__()

        self.logger.debug(message)

    def warning(self, message=None):
        self.__init__()

        self.logger.warning(message)

    def error(self, message=None):
        self.__init__()

        self.logger.error(message)

    def critical(self, message=None):
        self.__init__()

        self.logger.critical(message)

    def log(self, level, msg):
        if level == 'DEBUG':
            self.debug(msg)
        elif level == 'INFO':
            self.info(msg)
        elif level == 'WARNING' or level == 'WARN':
            self.warning(msg)
        elif level == 'ERROR':
            self.error(msg)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            with open(self.error_log_path, 'a') as f:
                f.write(str(current_time) + ' - ' + msg + '\n')
        elif level == 'CRITICAL':
            self.critical(msg)
        else:
            print('level should be DEBUG, INFO, WARNING, ERROR, CRITICAL.')
            self.info(msg)

        self.logger.removeHandler(self.logger.handlers)
        # 关闭句柄
        self.fh.close()
        self.ch.close()


def print_log_by_py_logger(level, msg):
    py_logger = Py_Logger()
    py_logger.log(level, msg)


def print_log(level, msg):
    """
    print msg to console and/or log file.

    When run in robot, print msg to console or log file(log.html).

    When not run in robot, print msg to console and log file:
    log in Linux: $HOME/log/autotest.log
    log in Windows: D:\\log\\autotest.log

    Args:
    | level | candidates are DEBUG, INFO, WARNING, ERROR |
    | msg   | log msg |
    """

    # get the caller's filename, lineno, ...
    # format: (filename, line number, function name, text)
    filename = '<empty>'
    lineno = 0
    # funcname = '<empty>'
    stack = traceback.extract_stack()
    if len(stack) >= 2:
        filename = os.path.basename(stack[-2][0])
        lineno = stack[-2][1]
        # funcname = stack[-2][2]
    # msg = '%s(%d):%s - %s' % (filename, lineno, funcname, msg)
    msg = '%s(%d) - %s' % (filename, lineno, msg)

    print_log_by_py_logger(level, msg)


if __name__ == '__main__':
    print_log('WARNING', 'warning message')
    print_log('INFO', 'Hello, World1')
    print_log('ERROR', 'Oops, not found!')
    print_log('DEBUG', 'debug info.')

