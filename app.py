#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from os import path

# 类似 node.js模块中 commandjs 针对命令行配置参数定义和处理
# tornado.options
# `options` 定义获取解析命令行参数的OptionsPerse 对象
# `define` 用于定义配置项
# `parse_command_line` 解析命令行参数
from tornado.options import options, define, parse_command_line
from tornado.httpserver import HTTPServer

from libs.utils import parse_config_file
from libs.route import handlers

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="web js is debug", type=bool)
define('num_processes', default=1, help="web server processes num", type=int)

class Application(tornado.web.Application):

    def __init__(self):
        settings = dict(
            debug=options.debug,
            # 设置前端静态文件夹路径
            static_path=path.join(path.dirname(__file__), "static"),
            template_path=path.join(path.dirname(__file__), "templates")
        )

        # **settings 配置
        super(Application, self).__init__(handlers, **settings)


def main():
    parse_config_file(path.join(path.dirname(__file__), "pyphoto.conf"))
    parse_command_line()

    http_server = HTTPServer(Application(), xheaders=True)

    http_server.bind(int(options.port))
    # 开启多线程服务
    http_server.start(options.num_processes)

    print 'tornado version:', tornado.version, options.description
    print 'server start by port ', options.port

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
