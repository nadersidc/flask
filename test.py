# encoding: utf-8
from flask import Flask

"""
@version: ??
@author: phpergao
@license: Apache Licence 
@contact: endoffight@gmail.com
@site: http://www.nadersidc.com
@software: PyCharm
@file: test.py
@time: 2017/4/21 下午10:40
"""
app = Flask(__name__)


@app.route('/')
def index():
    return 'hello flask'


if __name__ == '__main__':
    app.run(debug=True)
