from IntfGraphics import *
from LCLClasses import *
from GraphType import *
from Graphics import *
from Classes import *
from MainPasObject import *
import LCLBindingUtil
#import end
#class TChangeLink start
class TChangeLink(TObject):
#    pointer=c_void_p()
    def __init__(self):#TChangeLink
        TObject.__init__(self)
#Procedure ImgList_TChangeLink_Change
    @staticmethod
    def Change(self,):
        LCLBinding.ImgList_TChangeLink_Change()
    def _Warper_OnChange(self,Sender):
        self.OnChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangecall'):
            FreeOldEvent=1
            oldobj=self.OnChangePasObject
        self.OnChangecall=v 
        self.PasOnChange=FunctionForm(self._Warper_OnChange)
        self.OnChangePasObject=LCLBinding.set_ImgList_TChangeLink_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def getSender(self):
        r=LCLBinding.get_ImgList_TChangeLink_Sender(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomImageList)
    def setSender(self,v):
        LCLBinding.set_ImgList_TChangeLink_Sender(self.pointer,v.pointer)
    Sender=property(getSender,setSender)
#class TChangeLink end
#class TCustomImageList start
class TCustomImageList(TLCLReferenceComponent):
#    pointer=c_void_p()
    def __init__(self):#TCustomImageList
        TLCLReferenceComponent.__init__(self)
#constructorImgList_TCustomImageList_Create
    @staticmethod
    def Create(AOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ImgList_TCustomImageList_Create((AOwner.pointer)),TCustomImageList)
#constructorImgList_TCustomImageList_CreateSize
    @staticmethod
    def CreateSize(AWidth,AHeight):
        return LCLBindingUtil.GetPytonObject(LCLBinding.ImgList_TCustomImageList_CreateSize((AWidth),(AHeight)),TCustomImageList)
#Procedure ImgList_TCustomImageList_AssignTo
    @staticmethod
    def AssignTo(self,Dest):
        LCLBinding.ImgList_TCustomImageList_AssignTo((Dest.pointer))
#Procedure ImgList_TCustomImageList_Assign
    @staticmethod
    def Assign(self,Source):
        LCLBinding.ImgList_TCustomImageList_Assign((Source.pointer))
#Procedure ImgList_TCustomImageList_WriteData
    @staticmethod
    def WriteData(self,AStream):
        LCLBinding.ImgList_TCustomImageList_WriteData((AStream.pointer))
#Procedure ImgList_TCustomImageList_ReadData
    @staticmethod
    def ReadData(self,AStream):
        LCLBinding.ImgList_TCustomImageList_ReadData((AStream.pointer))
#Procedure ImgList_TCustomImageList_BeginUpdate
    @staticmethod
    def BeginUpdate(self,):
        LCLBinding.ImgList_TCustomImageList_BeginUpdate()
#Procedure ImgList_TCustomImageList_EndUpdate
    @staticmethod
    def EndUpdate(self,):
        LCLBinding.ImgList_TCustomImageList_EndUpdate()
#Procedure ImgList_TCustomImageList_AddImages
    @staticmethod
    def AddImages(self,AValue):
        LCLBinding.ImgList_TCustomImageList_AddImages((AValue.pointer))
#Procedure ImgList_TCustomImageList_Change
    @staticmethod
    def Change(self,):
        LCLBinding.ImgList_TCustomImageList_Change()
#Procedure ImgList_TCustomImageList_Clear
    @staticmethod
    def Clear(self,):
        LCLBinding.ImgList_TCustomImageList_Clear()
#Procedure ImgList_TCustomImageList_Delete
    @staticmethod
    def Delete(self,AIndex):
        LCLBinding.ImgList_TCustomImageList_Delete((AIndex))
#Procedure ImgList_TCustomImageList_GetFullBitmap
    @staticmethod
    def GetFullBitmap(self,Image,AEffect):
        LCLBinding.ImgList_TCustomImageList_GetFullBitmap((Image.pointer),(AEffect.pointer))
#Procedure ImgList_TCustomImageList_Insert
    @staticmethod
    def Insert(self,AIndex,AImage,AMask):
        LCLBinding.ImgList_TCustomImageList_Insert((AIndex),(AImage.pointer),(AMask.pointer))
#Procedure ImgList_TCustomImageList_InsertIcon
    @staticmethod
    def InsertIcon(self,AIndex,AIcon):
        LCLBinding.ImgList_TCustomImageList_InsertIcon((AIndex),(AIcon.pointer))
#Procedure ImgList_TCustomImageList_Move
    @staticmethod
    def Move(self,ACurIndex,ANewIndex):
        LCLBinding.ImgList_TCustomImageList_Move((ACurIndex),(ANewIndex))
    def getHasOverlays(self):
        r=LCLBinding.get_ImgList_TCustomImageList_HasOverlays(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    HasOverlays=property(getHasOverlays)
#Procedure ImgList_TCustomImageList_Replace
    @staticmethod
    def Replace(self,AIndex,AImage,AMask):
        LCLBinding.ImgList_TCustomImageList_Replace((AIndex),(AImage.pointer),(AMask.pointer))
#Procedure ImgList_TCustomImageList_RegisterChanges
    @staticmethod
    def RegisterChanges(self,Value):
        LCLBinding.ImgList_TCustomImageList_RegisterChanges((Value.pointer))
#Procedure ImgList_TCustomImageList_UnRegisterChanges
    @staticmethod
    def UnRegisterChanges(self,Value):
        LCLBinding.ImgList_TCustomImageList_UnRegisterChanges((Value.pointer))
    def getAllocBy(self):
        r=LCLBinding.get_ImgList_TCustomImageList_AllocBy(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setAllocBy(self,v):
        LCLBinding.set_ImgList_TCustomImageList_AllocBy(self.pointer,v)
    AllocBy=property(getAllocBy,setAllocBy)
    def getCount(self):
        r=LCLBinding.get_ImgList_TCustomImageList_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
    def getDrawingStyle(self):
        r=LCLBinding.get_ImgList_TCustomImageList_DrawingStyle(self.pointer)
        return r
    def setDrawingStyle(self,v):
        LCLBinding.set_ImgList_TCustomImageList_DrawingStyle(self.pointer,v.pointer)
    DrawingStyle=property(getDrawingStyle,setDrawingStyle)
    def getHeight(self):
        r=LCLBinding.get_ImgList_TCustomImageList_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setHeight(self,v):
        LCLBinding.set_ImgList_TCustomImageList_Height(self.pointer,v)
    Height=property(getHeight,setHeight)
    def getWidth(self):
        r=LCLBinding.get_ImgList_TCustomImageList_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setWidth(self,v):
        LCLBinding.set_ImgList_TCustomImageList_Width(self.pointer,v)
    Width=property(getWidth,setWidth)
    def _Warper_OnChange(self,Sender):
        self.OnChangecall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChange(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangecall'):
            FreeOldEvent=1
            oldobj=self.OnChangePasObject
        self.OnChangecall=v 
        self.PasOnChange=FunctionForm(self._Warper_OnChange)
        self.OnChangePasObject=LCLBinding.set_ImgList_TCustomImageList_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def getMasked(self):
        r=LCLBinding.get_ImgList_TCustomImageList_Masked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setMasked(self,v):
        LCLBinding.set_ImgList_TCustomImageList_Masked(self.pointer,v)
    Masked=property(getMasked,setMasked)
    def getShareImages(self):
        r=LCLBinding.get_ImgList_TCustomImageList_ShareImages(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setShareImages(self,v):
        LCLBinding.set_ImgList_TCustomImageList_ShareImages(self.pointer,v)
    ShareImages=property(getShareImages,setShareImages)
    def getImageType(self):
        r=LCLBinding.get_ImgList_TCustomImageList_ImageType(self.pointer)
        return r
    def setImageType(self,v):
        LCLBinding.set_ImgList_TCustomImageList_ImageType(self.pointer,v.pointer)
    ImageType=property(getImageType,setImageType)
#class TCustomImageList end
