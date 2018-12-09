from ctypes import *
LCLBinding=cdll.LoadLibrary("G:\\dev\\temp\\lclbinding2\\parser\\generated\\python\\pas\\lclbinding.dll");
class TObject(object):
    def __init__(self):
        pointer=c_void_p()
