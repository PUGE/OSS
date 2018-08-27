# -*- coding: utf-8 -*-
import io
import oss2
import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  file_object = io.open('index.html','r', encoding='UTF-8')
  return file_object.read()

# 获取服务器信息
@app.route('/service/<accessKey>/<secret>')
def hello(accessKey, secret):
  auth = oss2.Auth(accessKey, secret)
  service = oss2.Service(auth, 'http://oss-cn-beijing.aliyuncs.com')
  return json.dumps([b.name for b in oss2.BucketIterator(service)])

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)