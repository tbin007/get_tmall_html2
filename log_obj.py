#! /usr/bin/env python
# coding=gbk
import logging, os


class Logger:
    def __init__(self, path, clevel=logging.DEBUG, Flevel=logging.DEBUG):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        # ����CMD��־
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)
        # �����ļ���־
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logyyx = Logger('.\\log\\log.log', logging.ERROR, logging.DEBUG)
    logyyx.debug('һ��debug��Ϣ')
    logyyx.info('һ��info��Ϣ')
    logyyx.war('һ��warning��Ϣ')
    logyyx.error('һ��error��Ϣ')
    logyyx.cri('һ������critical��Ϣ')