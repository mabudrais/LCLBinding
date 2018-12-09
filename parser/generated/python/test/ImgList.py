from MainPasObject import *
#import end
#class TCustomImageList start
class TCustomImageList(TLCLReferenceComponent):
#    pointer=c_void_p()
    def __init__(self):#TCustomImageList
        TLCLReferenceComponent.__init__(self)
#constructorImgList_TCustomImageList_Create
    def Create(cls,AOwner):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.ImgList_TCustomImageList_Create((AOwner.pointer)),TCustomImageList)
#constructorImgList_TCustomImageList_CreateSize
    def CreateSize(cls,AWidth,AHeight):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.ImgList_TCustomImageList_CreateSize((AWidth),(AHeight)),TCustomImageList)
    def getHasOverlays(self):
        r=LCLBinding.ImgList_TCustomImageList_HasOverlays(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    HasOverlays=property(getHasOverlays)
    def getAllocBy(self):
        r=LCLBinding.ImgList_TCustomImageList_AllocBy(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    AllocBy=property(getAllocBy)
    def getCount(self):
        r=LCLBinding.ImgList_TCustomImageList_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
    def getHeight(self):
        r=LCLBinding.ImgList_TCustomImageList_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
    def getWidth(self):
        r=LCLBinding.ImgList_TCustomImageList_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Width=property(getWidth)
    def getMasked(self):
        r=LCLBinding.ImgList_TCustomImageList_Masked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Masked=property(getMasked)
    def getShareImages(self):
        r=LCLBinding.ImgList_TCustomImageList_ShareImages(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    ShareImages=property(getShareImages)
#class TCustomImageList end
