# -*- coding: utf-8 -*-

# python 官方标准库
import os
import time
import StringIO
import tempfile

# pip 安装模块库
import Image
import tornado.web

from bson.objectid import ObjectId

# 自身应用模块
from libs.dbconn import mongodb, fs

# 注册后端路由处理机制
class MainHandler(tornado.web.RequestHandler):

    """docstring for AboutHandler"""
    def get(self):
        self.write("welcome to PyPhoto.")

class AboutHandler(tornado.web.RequestHandler):

    """docstring for AboutHandler"""
    def get(self):
        self.write("by Nightink")

class UploadHandler(tornado.web.RequestHandler):

    """图片上传响应handler"""

    def post(self):
        """图片上传"""

        if self.request.files:

            for imageFile in self.request.files['file']:

                raw_name = imageFile['filename']
                content_type = imageFile['content_type']
                file_body = imageFile['body']

                dst_name = str(int(time.time())) + '.' + raw_name.split('.').pop()

                thb_name = "thumb_" + dst_name

                tf = tempfile.NamedTemporaryFile()

                tf.write(file_body)
                tf.seek(0)

                data = StringIO.StringIO()

                img = Image.open(tf.name)

                format = img.format
                # 保存上传图片至mongodb
                img.save(data, format)
                id = fs.put(data.getvalue(), filename=dst_name, format=format, contentType=content_type)

                thum_data = StringIO.StringIO()
                img.thumbnail((200, 200), resample=1)
                img.save(thum_data, format)
                # 保存缩略图片至mongodb
                thum_id = fs.put(thum_data.getvalue(), filename=thb_name, format=format, contentType=content_type)

                tf.close()

            link_attachment_id = '<a href="/attachment/%s">原图</a>' % id
            link_attachment_thum_id = '<a href="/attachment/%s">缩略图</a>' % thum_id
            self.write(link_attachment_id + link_attachment_thum_id)


class AttachmentHandler(tornado.web.RequestHandler):

    """docstring for AttachmentHandler"""
    def get(self, name):
        gf = fs.get(ObjectId(name))
        im = gf.read()

        print name, gf.content_type
        self.set_header('content-type', gf.content_type or 'image/jpeg')
        self.write(im)

    def delete(self, name):
        print "delete ObjectId is ", name

class UserHandler(tornado.web.RequestHandler):

    """docstring for UserHandler"""

    def get(self):
        pass

