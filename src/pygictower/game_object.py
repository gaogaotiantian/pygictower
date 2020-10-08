# Licensed under the Apache License: http://www.apache.org/licenses/LICENSE-2.0
# For details: https://github.com/gaogaotiantian/pygictower/blob/master/NOTICE

class GameObject:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)
            else:
                raise TypeError("Unexpected keyword argument {}".format(key))
