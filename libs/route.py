# -*- coding: utf-8 -*-

# import tornado.web

# 导入路由hanler处理模块
from libs.hanler import MainHandler, AboutHandler, UploadHandler, AttachmentHandler, UserHandler


handlers = [
    (r"/", MainHandler),
    (r"/about", AboutHandler),
    (r"/upload", UploadHandler),
    (r"/attachment/([0-9a-z]+)", AttachmentHandler),
    (r"/user/([0-9a-z]+)", UserHandler),
    (r"/user", UserHandler)
]


    # (r"/user/([0-9a-z]+)", UserHandler),
    # (r"/user", UserHandler),
    # (r"/upload", UploadHandler),
    # (r"/attachment/([0-9a-z]+)", AttachmentHandler),
    # (r"/photo", PhotoHandler),
    # (r"/photo/([0-9a-z]+)", PhotoHandler),
    # (r"/po-photo", PhotoHandler),
    # # 用户删除图片路由注册
    # (r"/photo-delete", PhotoHandler),
    # # 用户更新图片信息路由注册
    # (r"/photo-update", UpdatePhotoHandler),
    # (r"/add-user", PostUserHandler),
    # # 用户更新图片信息路由注册
    # (r"/user-update", UpdateUserHandler),
    # 用户登陆
    # (r"/login", LoginHandler)
