import logging
import os
import time

class Log:
    def __init__(self):
        # 文件的命名
        log_path = self.logpath()
        # print(log_path)
        if os.path.exists(log_path):
            pass
        else:
            os.makedirs(log_path)
        # self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d_%H_%M_%S'))
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '[%(asctime)s]-%(filename)s[line:%(lineno)d]-fuc:%(funcName)s-%(levelname)s:%(message)s')

    def logpath(self):
        # logdir=os.path.split(os.path.realpath(os.getcwd()))[0]
        # logpath = os.path.join(logdir, 'log')
        curPath = os.path.abspath(os.path.dirname(__file__))
        rootPath = os.path.split(curPath)[0]
        logpath = os.path.join(rootPath, 'log')
        return logpath

    def __console(self, level, message):
        # 创建一个filehandler，用于写到本地
        fh = logging.FileHandler(self.logname, 'a')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个streamhandler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)

    logging.shutdown()


if __name__ == '__main__':
    pass
