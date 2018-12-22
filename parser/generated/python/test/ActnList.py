from LCLClasses import *
from ImgList import *
from Classes import *
from MainPasObject import *
#import end
#class TActionLink start
class TActionLink(TBasicActionLink):
#    pointer=c_void_p()
    def __init__(self):#TActionLink
        TBasicActionLink.__init__(self)
#constructorActnList_TActionLink_Create
    @staticmethod
    def Create(AClient):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ActnList_TActionLink_Create((AClient.pointer)),TActionLink)
#class TActionLink end
