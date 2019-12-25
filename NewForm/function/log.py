import logging
class Logger:
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        logging.captureWarnings(True) #不打印警告信息
        self.logger = logging.getLogger(path) #定义日志文件路径名字
        self.logger.setLevel(logging.DEBUG) #定义日志文件为debug级别
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S') #设置日志格式
        # 设置CMD日志
        sh = logging.StreamHandler()  #CMD环境运行显示log
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # 设置文件日志
        fh = logging.FileHandler(path) #文件路径名字
        fh.setFormatter(fmt) #日志文件格式
        fh.setLevel(Flevel) #日志文件等级
        self.logger.addHandler(sh) #cmd日志写入文件
        self.logger.addHandler(fh) #文本日志
    def debug(self, message):#诊断错误时候的详细信息
        self.logger.debug(message)
    def info(self, message):#程序正常运行，用来确认信息
        self.logger.info(message)
    def warn(self, message):#程序正常运行，但是警告某个未来可能发生的问题，或者未预料的事情
        self.logger.warning(message)
    def error(self, message): #严重问题，某些功能无法实现
        self.logger.error(message)
    def cri(self, message): #严重错误，程序无法运行
        self.logger.critical(message)