# Written by Timothy R. Chavez <timrchavez@gmail.com>


import exceptions
import random
import webbrowser


SCOTT_HOY_PSA = "https://youtu.be/C6eXBGOe-g4?t=24s"


class scotthoy(object):
    class VideoGameException(exceptions.Exception):
        def __init__(self,*args,**kwargs):
            Exception.__init__(self,*args,**kwargs)

    class HwatException(exceptions.Exception):
        def __init__(self,*args,**kwargs):
            Exception.__init__(self,*args,**kwargs)

    def __enter__(self):
        pass

    def __exit__(self, return_type, value, traceback):
        if isinstance(return_type, type(exceptions.Exception)):
            r = random.randint(0,1)
            raise (self.VideoGameException, self.HwatException)[r]

    @classmethod
    def will_you_please_stop(cls):
        webbrowser.open(SCOTT_HOY_PSA)

