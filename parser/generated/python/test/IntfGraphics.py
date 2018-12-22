from icnstypes import *
from GraphType import *
from Classes import *
from MainPasObject import *
#import end
#class TLazIntfImage start
class TLazIntfImage(TObject):
#    pointer=c_void_p()
    def __init__(self):#TLazIntfImage
        TObject.__init__(self)
#constructorIntfGraphics_TLazIntfImage_CreateCompatible
    @staticmethod
    def CreateCompatible(IntfImg,AWidth,AHeight):
        return LCLBindingUtil.GetPytonObject(LCLBinding.IntfGraphics_TLazIntfImage_CreateCompatible((IntfImg.pointer),(AWidth),(AHeight)),TLazIntfImage)
#Procedure IntfGraphics_TLazIntfImage_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.IntfGraphics_TLazIntfImage_Assign((Source.pointer))
#Procedure IntfGraphics_TLazIntfImage_BeginUpdate
    @staticmethod
    def BeginUpdate(self,):
        LCLBinding.IntfGraphics_TLazIntfImage_BeginUpdate()
#Procedure IntfGraphics_TLazIntfImage_EndUpdate
    @staticmethod
    def EndUpdate(self,):
        LCLBinding.IntfGraphics_TLazIntfImage_EndUpdate()
#Procedure IntfGraphics_TLazIntfImage_SetSize
    @staticmethod
    def SetSize(self,AWidth,AHeight):
        LCLBinding.IntfGraphics_TLazIntfImage_SetSize((AWidth),(AHeight))
#Procedure IntfGraphics_TLazIntfImage_SetRawImage
    @staticmethod
    def SetRawImage(self,ARawImage,ADataOwner):
        LCLBinding.IntfGraphics_TLazIntfImage_SetRawImage((ARawImage.pointer),(booleantoint(ADataOwner)))
#Procedure IntfGraphics_TLazIntfImage_AlphaBlend
    @staticmethod
    def AlphaBlend(self,ASource,ASourceAlpha,ADestX,ADestY):
        LCLBinding.IntfGraphics_TLazIntfImage_AlphaBlend((ASource.pointer),(ASourceAlpha.pointer),(ADestX),(ADestY))
#Procedure IntfGraphics_TLazIntfImage_AlphaFromMask
    @staticmethod
    def AlphaFromMask(self,AKeepAlpha):
        LCLBinding.IntfGraphics_TLazIntfImage_AlphaFromMask((booleantoint(AKeepAlpha)))
#Procedure IntfGraphics_TLazIntfImage_CreateData
    @staticmethod
    def CreateData(self,):
        LCLBinding.IntfGraphics_TLazIntfImage_CreateData()
#Procedure IntfGraphics_TLazIntfImage_SetDataDescriptionKeepData
    @staticmethod
    def SetDataDescriptionKeepData(self,ADescription):
        LCLBinding.IntfGraphics_TLazIntfImage_SetDataDescriptionKeepData((ADescription.pointer))
    def getDataDescription(self):
        r=LCLBinding.get_IntfGraphics_TLazIntfImage_DataDescription(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TRawImageDescription)
    def setDataDescription(self,v):
        LCLBinding.set_IntfGraphics_TLazIntfImage_DataDescription(self.pointer,v.pointer)
    DataDescription=property(getDataDescription,setDataDescription)
    def getMasked(self,x,y):
        r=LCLBinding.get_IntfGraphics_TLazIntfImage_Masked(self.pointer,x,y)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setMasked(self,x,y,v):
        LCLBinding.set_IntfGraphics_TLazIntfImage_Masked(self.pointer,x,y,v)
#class TLazIntfImage end
