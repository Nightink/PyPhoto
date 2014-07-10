# -*- coding: utf-8 -*-

from pymongo import Connection
from gridfs import GridFS

conn = Connection("mongodb://mongodb:mongodb@127.0.0.1:27017")

mongodb = conn['pyphoto']

fs = GridFS(mongodb, 'images')
