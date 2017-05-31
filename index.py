#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import tornado.ioloop
import tornado.web
from config import url


if __name__ == "__main__":
    port = 8800
    setting = dict(
      template_path = os.path.join(os.path.dirname(__file__), "templates"),
      static_path = os.path.join(os.path.dirname(__file__), "static"),
      debug = True
    )
    app = tornado.web.Application(handlers=url.urls, **setting)
    app.listen(port)
    print("* Successfully started.")
    print("* Listening on port: %s" % port)
    print("* Press Ctrl+C to shutdown.")
    tornado.ioloop.IOLoop.current().start()
