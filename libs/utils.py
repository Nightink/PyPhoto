# -*- coding: utf-8 -*-

from tornado.options import define, options


def parse_config_file(path):
    """重写tornado.options 默认parese_config_file函数
    解析并载入指定的路径 python配置文件
    允许对未定义参数，进行配置处理
    """

    config = {}
    execfile(path, config, config)

    for name in config:
        if name in options:
            # options[name] = config[name] # TypeError: 'OptionParser' object does not support item assignment
            # 设置实例属性
            setattr(options, name, config[name])
        else:
            define(name, config[name])
