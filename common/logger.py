import logging


def setup_logger():
    # 日志记录器logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # 文件处理器，将日志写入文件
    file_handler = logging.FileHandler('logs/test.log')
    file_handler.setLevel(logging.INFO)
    # 控制台处理器，将日志输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    # 日志格式
    formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)

    return logger


logger = setup_logger()