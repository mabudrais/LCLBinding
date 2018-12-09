from MainPasObject import *
#import end
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
    def getHasOverlays(self):
        r=LCLBinding.get_ImgList_TCustomImageList_HasOverlays(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    HasOverlays=property(getHasOverlays)
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
            oldobj=OnChangePasObject
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
