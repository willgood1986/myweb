# -*- coding: utf-8 -*-

class Dict(dict):
    def __init__(self, **kargs):
        super().__init__(**kargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"Dict has no object by key '%s'" %key)

    def __setattr__(self, key, val):
        self[key] = val
