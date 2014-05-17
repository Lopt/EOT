# -*- coding: utf-8 -*-

import json


class ObjectEncoder(json.JSONEncoder):
     def default(self, obj):
         if isinstance(obj, object):
             return obj.__dict__
         # Let the base class default method raise the TypeError
         return json.JSONEncoder.default(self, obj)