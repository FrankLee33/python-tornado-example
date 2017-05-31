#!/usr/bin/env python
# -*- coding:utf-8 -*-

from controllers import (user, default)

urls=[
    (r"/", default.Index),
    (r"/ueditor/upload/", default.RemotePicture),
    (r"/login", user.Login),
    (r"/logout", user.Logout)
]
