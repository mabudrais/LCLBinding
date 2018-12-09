from MainPasObject import *
#import end
#class TCustomIcon start
class TCustomIcon(TRasterImage):
#    pointer=c_void_p()
    def __init__(self):#TCustomIcon
        TRasterImage.__init__(self)
#constructorGraphics_TCustomIcon_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TCustomIcon_Create(),TCustomIcon)
    def getCurrent(self):
        r=LCLBinding.Graphics_TCustomIcon_Current(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Current=property(getCurrent)
    def getCount(self):
        r=LCLBinding.Graphics_TCustomIcon_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
#class TCustomIcon end
#class TIcon start
class TIcon(TCustomIcon):
#    pointer=c_void_p()
    def __init__(self):#TIcon
        TCustomIcon.__init__(self)
#class TIcon end
#class TGraphicsObject start
class TGraphicsObject(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TGraphicsObject
        TPersistent.__init__(self)
#class TGraphicsObject end
#class TRegion start
class TRegion(TGraphicsObject):
#    pointer=c_void_p()
    def __init__(self):#TRegion
        TGraphicsObject.__init__(self)
#constructorGraphics_TRegion_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TRegion_Create(),TRegion)
#class TRegion end
#class TPen start
class TPen(TFPCustomPen):
#    pointer=c_void_p()
    def __init__(self):#TPen
        TFPCustomPen.__init__(self)
#constructorGraphics_TPen_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TPen_Create(),TPen)
    def getCosmetic(self):
        r=LCLBinding.Graphics_TPen_Cosmetic(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Cosmetic=property(getCosmetic)
#class TPen end
#class TBrush start
class TBrush(TFPCustomBrush):
#    pointer=c_void_p()
    def __init__(self):#TBrush
        TFPCustomBrush.__init__(self)
#constructorGraphics_TBrush_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TBrush_Create(),TBrush)
#class TBrush end
#class TCanvas start
class TCanvas(TFPCustomCanvas):
#    pointer=c_void_p()
    def __init__(self):#TCanvas
        TFPCustomCanvas.__init__(self)
#constructorGraphics_TCanvas_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TCanvas_Create(),TCanvas)
    def getAutoRedraw(self):
        r=LCLBinding.Graphics_TCanvas_AutoRedraw(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    AutoRedraw=property(getAutoRedraw)
    def getBrush(self):
        r=LCLBinding.Graphics_TCanvas_Brush(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TBrush)
    Brush=property(getBrush)
    def getFont(self):
        r=LCLBinding.Graphics_TCanvas_Font(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TFont)
    Font=property(getFont)
    def getHeight(self):
        r=LCLBinding.Graphics_TCanvas_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
    def getPen(self):
        r=LCLBinding.Graphics_TCanvas_Pen(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TPen)
    Pen=property(getPen)
    def getRegion(self):
        r=LCLBinding.Graphics_TCanvas_Region(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TRegion)
    Region=property(getRegion)
    def getWidth(self):
        r=LCLBinding.Graphics_TCanvas_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Width=property(getWidth)
#class TCanvas end
#class TGraphic start
class TGraphic(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TGraphic
        TPersistent.__init__(self)
#constructorGraphics_TGraphic_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TGraphic_Create(),TGraphic)
    def getEmpty(self):
        r=LCLBinding.Graphics_TGraphic_Empty(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Empty=property(getEmpty)
    def getHeight(self):
        r=LCLBinding.Graphics_TGraphic_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
    def getModified(self):
        r=LCLBinding.Graphics_TGraphic_Modified(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Modified=property(getModified)
    def getPaletteModified(self):
        r=LCLBinding.Graphics_TGraphic_PaletteModified(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    PaletteModified=property(getPaletteModified)
    def getTransparent(self):
        r=LCLBinding.Graphics_TGraphic_Transparent(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Transparent=property(getTransparent)
    def getWidth(self):
        r=LCLBinding.Graphics_TGraphic_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Width=property(getWidth)
#class TGraphic end
#class TRasterImage start
class TRasterImage(TGraphic):
#    pointer=c_void_p()
    def __init__(self):#TRasterImage
        TGraphic.__init__(self)
#constructorGraphics_TRasterImage_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TRasterImage_Create(),TRasterImage)
    def getCanvas(self):
        r=LCLBinding.Graphics_TRasterImage_Canvas(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TCanvas)
    Canvas=property(getCanvas)
    def getMasked(self):
        r=LCLBinding.Graphics_TRasterImage_Masked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Masked=property(getMasked)
    def getRawImage(self):
        r=LCLBinding.Graphics_TRasterImage_RawImage(self.pointer)
        return LCLBindingUtil.ConvertPascalpointer(r,TRawImage)
    RawImage=property(getRawImage)
#class TRasterImage end
#class TCustomBitmap start
class TCustomBitmap(TRasterImage):
#    pointer=c_void_p()
    def __init__(self):#TCustomBitmap
        TRasterImage.__init__(self)
#constructorGraphics_TCustomBitmap_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TCustomBitmap_Create(),TCustomBitmap)
    def getMonochrome(self):
        r=LCLBinding.Graphics_TCustomBitmap_Monochrome(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Monochrome=property(getMonochrome)
#class TCustomBitmap end
#class TFPImageBitmap start
class TFPImageBitmap(TCustomBitmap):
#    pointer=c_void_p()
    def __init__(self):#TFPImageBitmap
        TCustomBitmap.__init__(self)
#class TFPImageBitmap end
#class TBitmap start
class TBitmap(TFPImageBitmap):
#    pointer=c_void_p()
    def __init__(self):#TBitmap
        TFPImageBitmap.__init__(self)
#class TBitmap end
#class TFont start
class TFont(TFPCustomFont):
#    pointer=c_void_p()
    def __init__(self):#TFont
        TFPCustomFont.__init__(self)
#constructorGraphics_TFont_Create
    def Create(cls):
        r=LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TFont_Create(),TFont)
    def getIsMonoSpace(self):
        r=LCLBinding.Graphics_TFont_IsMonoSpace(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    IsMonoSpace=property(getIsMonoSpace)
    def getCanUTF8(self):
        r=LCLBinding.Graphics_TFont_CanUTF8(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    CanUTF8=property(getCanUTF8)
    def getPixelsPerInch(self):
        r=LCLBinding.Graphics_TFont_PixelsPerInch(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    PixelsPerInch=property(getPixelsPerInch)
    def getHeight(self):
        r=LCLBinding.Graphics_TFont_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
    def getOrientation(self):
        r=LCLBinding.Graphics_TFont_Orientation(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Orientation=property(getOrientation)
    def getSize(self):
        r=LCLBinding.Graphics_TFont_Size(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Size=property(getSize)
#class TFont end
