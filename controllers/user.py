#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tornado.web import (RequestHandler)

class Login(RequestHandler):
    def get(self):
        self.write("login page")

class Logout(RequestHandler):
    def get(self):
        self.write("logout page")
