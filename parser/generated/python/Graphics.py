from MainPasObject import *
#import end
def CreateTFontStylesFromInt(i):
    dic={1:"fsBold",2:"fsItalic",4:"fsUnderline",8:"fsStrikeOut"}
    return CreateSetFormint(i,dic)
#class TGraphic start
class TGraphic(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TGraphic
        TPersistent.__init__(self)
#constructorGraphics_TGraphic_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TGraphic_Create(),TGraphic)
    def getEmpty(self):
        r=LCLBinding.get_Graphics_TGraphic_Empty(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    Empty=property(getEmpty)
    def getHeight(self):
        r=LCLBinding.get_Graphics_TGraphic_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setHeight(self,v):
        LCLBinding.set_Graphics_TGraphic_Height(self.pointer,v)
    Height=property(getHeight,setHeight)
    def getModified(self):
        r=LCLBinding.get_Graphics_TGraphic_Modified(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setModified(self,v):
        LCLBinding.set_Graphics_TGraphic_Modified(self.pointer,v)
    Modified=property(getModified,setModified)
    def getMimeType(self):
        r=LCLBinding.get_Graphics_TGraphic_MimeType(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    MimeType=property(getMimeType)
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
        self.OnChangePasObject=LCLBinding.set_Graphics_TGraphic_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def getPaletteModified(self):
        r=LCLBinding.get_Graphics_TGraphic_PaletteModified(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setPaletteModified(self,v):
        LCLBinding.set_Graphics_TGraphic_PaletteModified(self.pointer,v)
    PaletteModified=property(getPaletteModified,setPaletteModified)
    def getTransparent(self):
        r=LCLBinding.get_Graphics_TGraphic_Transparent(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setTransparent(self,v):
        LCLBinding.set_Graphics_TGraphic_Transparent(self.pointer,v)
    Transparent=property(getTransparent,setTransparent)
    def getWidth(self):
        r=LCLBinding.get_Graphics_TGraphic_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setWidth(self,v):
        LCLBinding.set_Graphics_TGraphic_Width(self.pointer,v)
    Width=property(getWidth,setWidth)
#class TGraphic end
#class TRasterImage start
class TRasterImage(TGraphic):
#    pointer=c_void_p()
    def __init__(self):#TRasterImage
        TGraphic.__init__(self)
#constructorGraphics_TRasterImage_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TRasterImage_Create(),TRasterImage)
    def getCanvas(self):
        r=LCLBinding.get_Graphics_TRasterImage_Canvas(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCanvas)
    Canvas=property(getCanvas)
    def getMasked(self):
        r=LCLBinding.get_Graphics_TRasterImage_Masked(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setMasked(self,v):
        LCLBinding.set_Graphics_TRasterImage_Masked(self.pointer,v)
    Masked=property(getMasked,setMasked)
    def getPixelFormat(self):
        r=LCLBinding.get_Graphics_TRasterImage_PixelFormat(self.pointer)
        return r
    def setPixelFormat(self,v):
        LCLBinding.set_Graphics_TRasterImage_PixelFormat(self.pointer,v.pointer)
    PixelFormat=property(getPixelFormat,setPixelFormat)
    def getRawImage(self):
        r=LCLBinding.get_Graphics_TRasterImage_RawImage(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TRawImage)
    RawImage=property(getRawImage)
    def getTransparentMode(self):
        r=LCLBinding.get_Graphics_TRasterImage_TransparentMode(self.pointer)
        return r
    def setTransparentMode(self,v):
        LCLBinding.set_Graphics_TRasterImage_TransparentMode(self.pointer,v.pointer)
    TransparentMode=property(getTransparentMode,setTransparentMode)
#class TRasterImage end
#class TCustomBitmap start
class TCustomBitmap(TRasterImage):
#    pointer=c_void_p()
    def __init__(self):#TCustomBitmap
        TRasterImage.__init__(self)
#constructorGraphics_TCustomBitmap_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TCustomBitmap_Create(),TCustomBitmap)
    def getHandleType(self):
        r=LCLBinding.get_Graphics_TCustomBitmap_HandleType(self.pointer)
        return r
    def setHandleType(self,v):
        LCLBinding.set_Graphics_TCustomBitmap_HandleType(self.pointer,v.pointer)
    HandleType=property(getHandleType,setHandleType)
    def getMonochrome(self):
        r=LCLBinding.get_Graphics_TCustomBitmap_Monochrome(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setMonochrome(self,v):
        LCLBinding.set_Graphics_TCustomBitmap_Monochrome(self.pointer,v)
    Monochrome=property(getMonochrome,setMonochrome)
#class TCustomBitmap end
#class TFPImageBitmap start
class TFPImageBitmap(TCustomBitmap):
#    pointer=c_void_p()
    def __init__(self):#TFPImageBitmap
        TCustomBitmap.__init__(self)
#constructorGraphics_TFPImageBitmap_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TFPImageBitmap_Create(),TFPImageBitmap)
#class TFPImageBitmap end
#class TPicture start
class TPicture(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TPicture
        TPersistent.__init__(self)
#constructorGraphics_TPicture_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TPicture_Create(),TPicture)
    def getBitmap(self):
        r=LCLBinding.get_Graphics_TPicture_Bitmap(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBitmap)
    def setBitmap(self,v):
        LCLBinding.set_Graphics_TPicture_Bitmap(self.pointer,v.pointer)
    Bitmap=property(getBitmap,setBitmap)
    def getIcon(self):
        r=LCLBinding.get_Graphics_TPicture_Icon(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TIcon)
    def setIcon(self,v):
        LCLBinding.set_Graphics_TPicture_Icon(self.pointer,v.pointer)
    Icon=property(getIcon,setIcon)
    def getJpeg(self):
        r=LCLBinding.get_Graphics_TPicture_Jpeg(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TJpegImage)
    def setJpeg(self,v):
        LCLBinding.set_Graphics_TPicture_Jpeg(self.pointer,v.pointer)
    Jpeg=property(getJpeg,setJpeg)
    def getPixmap(self):
        r=LCLBinding.get_Graphics_TPicture_Pixmap(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPixmap)
    def setPixmap(self,v):
        LCLBinding.set_Graphics_TPicture_Pixmap(self.pointer,v.pointer)
    Pixmap=property(getPixmap,setPixmap)
    def getPNG(self):
        r=LCLBinding.get_Graphics_TPicture_PNG(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPortableNetworkGraphic)
    def setPNG(self,v):
        LCLBinding.set_Graphics_TPicture_PNG(self.pointer,v.pointer)
    PNG=property(getPNG,setPNG)
    def getPNM(self):
        r=LCLBinding.get_Graphics_TPicture_PNM(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPortableAnyMapGraphic)
    def setPNM(self,v):
        LCLBinding.set_Graphics_TPicture_PNM(self.pointer,v.pointer)
    PNM=property(getPNM,setPNM)
    def getGraphic(self):
        r=LCLBinding.get_Graphics_TPicture_Graphic(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TGraphic)
    def setGraphic(self,v):
        LCLBinding.set_Graphics_TPicture_Graphic(self.pointer,v.pointer)
    Graphic=property(getGraphic,setGraphic)
    def getHeight(self):
        r=LCLBinding.get_Graphics_TPicture_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
    def getWidth(self):
        r=LCLBinding.get_Graphics_TPicture_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Width=property(getWidth)
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
        self.OnChangePasObject=LCLBinding.set_Graphics_TPicture_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
#class TPicture end
#class TJPEGImage start
class TJPEGImage(TFPImageBitmap):
#    pointer=c_void_p()
    def __init__(self):#TJPEGImage
        TFPImageBitmap.__init__(self)
#constructorGraphics_TJPEGImage_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TJPEGImage_Create(),TJPEGImage)
    def getGrayScale(self):
        r=LCLBinding.get_Graphics_TJPEGImage_GrayScale(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    GrayScale=property(getGrayScale)
    def getProgressiveEncoding(self):
        r=LCLBinding.get_Graphics_TJPEGImage_ProgressiveEncoding(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    ProgressiveEncoding=property(getProgressiveEncoding)
#class TJPEGImage end
#class TPixmap start
class TPixmap(TFPImageBitmap):
#    pointer=c_void_p()
    def __init__(self):#TPixmap
        TFPImageBitmap.__init__(self)
#constructorGraphics_TPixmap_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TPixmap_Create(),TPixmap)
#class TPixmap end
#class TGraphicsObject start
class TGraphicsObject(TPersistent):
#    pointer=c_void_p()
    def __init__(self):#TGraphicsObject
        TPersistent.__init__(self)
    def _Warper_OnChanging(self,Sender):
        self.OnChangingcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChanging(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangingcall'):
            FreeOldEvent=1
            oldobj=OnChangingPasObject
        self.OnChangingcall=v 
        self.PasOnChanging=FunctionForm(self._Warper_OnChanging)
        self.OnChangingPasObject=LCLBinding.set_Graphics_TGraphicsObject_OnChanging(self.pointer,self.PasOnChanging,oldobj,FreeOldEvent)
    def getOnChanging(self):
        return OnChangingcall
    OnChanging=property(getOnChanging,setOnChanging)
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
        self.OnChangePasObject=LCLBinding.set_Graphics_TGraphicsObject_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
#class TGraphicsObject end
#class TRegion start
class TRegion(TGraphicsObject):
#    pointer=c_void_p()
    def __init__(self):#TRegion
        TGraphicsObject.__init__(self)
#constructorGraphics_TRegion_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TRegion_Create(),TRegion)
#class TRegion end
#class TPen start
class TPen(TFPCustomPen):
#    pointer=c_void_p()
    def __init__(self):#TPen
        TFPCustomPen.__init__(self)
#constructorGraphics_TPen_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TPen_Create(),TPen)
    def getCosmetic(self):
        r=LCLBinding.get_Graphics_TPen_Cosmetic(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setCosmetic(self,v):
        LCLBinding.set_Graphics_TPen_Cosmetic(self.pointer,v)
    Cosmetic=property(getCosmetic,setCosmetic)
    def getEndCap(self):
        r=LCLBinding.get_Graphics_TPen_EndCap(self.pointer)
        return r
    def setEndCap(self,v):
        LCLBinding.set_Graphics_TPen_EndCap(self.pointer,v.pointer)
    EndCap=property(getEndCap,setEndCap)
    def getJoinStyle(self):
        r=LCLBinding.get_Graphics_TPen_JoinStyle(self.pointer)
        return r
    def setJoinStyle(self,v):
        LCLBinding.set_Graphics_TPen_JoinStyle(self.pointer,v.pointer)
    JoinStyle=property(getJoinStyle,setJoinStyle)
#class TPen end
#class TBrush start
class TBrush(TFPCustomBrush):
#    pointer=c_void_p()
    def __init__(self):#TBrush
        TFPCustomBrush.__init__(self)
#constructorGraphics_TBrush_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TBrush_Create(),TBrush)
    def getBitmap(self):
        r=LCLBinding.get_Graphics_TBrush_Bitmap(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TCustomBitmap)
    def setBitmap(self,v):
        LCLBinding.set_Graphics_TBrush_Bitmap(self.pointer,v.pointer)
    Bitmap=property(getBitmap,setBitmap)
#class TBrush end
#class TCanvas start
class TCanvas(TFPCustomCanvas):
#    pointer=c_void_p()
    def __init__(self):#TCanvas
        TFPCustomCanvas.__init__(self)
#constructorGraphics_TCanvas_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TCanvas_Create(),TCanvas)
    def getAntialiasingMode(self):
        r=LCLBinding.get_Graphics_TCanvas_AntialiasingMode(self.pointer)
        return r
    def setAntialiasingMode(self,v):
        LCLBinding.set_Graphics_TCanvas_AntialiasingMode(self.pointer,v.pointer)
    AntialiasingMode=property(getAntialiasingMode,setAntialiasingMode)
    def getAutoRedraw(self):
        r=LCLBinding.get_Graphics_TCanvas_AutoRedraw(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    def setAutoRedraw(self,v):
        LCLBinding.set_Graphics_TCanvas_AutoRedraw(self.pointer,v)
    AutoRedraw=property(getAutoRedraw,setAutoRedraw)
    def getBrush(self):
        r=LCLBinding.get_Graphics_TCanvas_Brush(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TBrush)
    def setBrush(self,v):
        LCLBinding.set_Graphics_TCanvas_Brush(self.pointer,v.pointer)
    Brush=property(getBrush,setBrush)
    def getFont(self):
        r=LCLBinding.get_Graphics_TCanvas_Font(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TFont)
    def setFont(self,v):
        LCLBinding.set_Graphics_TCanvas_Font(self.pointer,v.pointer)
    Font=property(getFont,setFont)
    def getHeight(self):
        r=LCLBinding.get_Graphics_TCanvas_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Height=property(getHeight)
    def getPen(self):
        r=LCLBinding.get_Graphics_TCanvas_Pen(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TPen)
    def setPen(self,v):
        LCLBinding.set_Graphics_TCanvas_Pen(self.pointer,v.pointer)
    Pen=property(getPen,setPen)
    def getRegion(self):
        r=LCLBinding.get_Graphics_TCanvas_Region(self.pointer)
        return LCLBindingUtil.GetPytonObject(r,TRegion)
    def setRegion(self,v):
        LCLBinding.set_Graphics_TCanvas_Region(self.pointer,v.pointer)
    Region=property(getRegion,setRegion)
    def getWidth(self):
        r=LCLBinding.get_Graphics_TCanvas_Width(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Width=property(getWidth)
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
        self.OnChangePasObject=LCLBinding.set_Graphics_TCanvas_OnChange(self.pointer,self.PasOnChange,oldobj,FreeOldEvent)
    def getOnChange(self):
        return OnChangecall
    OnChange=property(getOnChange,setOnChange)
    def _Warper_OnChanging(self,Sender):
        self.OnChangingcall(LCLBindingUtil.GetPytonObject(Sender,TObject))
    def setOnChanging(self,v):
        FunctionForm= CFUNCTYPE(c_void_p,c_void_p)
        FreeOldEvent=0
        oldobj=0
        if hasattr(self, 'OnChangingcall'):
            FreeOldEvent=1
            oldobj=OnChangingPasObject
        self.OnChangingcall=v 
        self.PasOnChanging=FunctionForm(self._Warper_OnChanging)
        self.OnChangingPasObject=LCLBinding.set_Graphics_TCanvas_OnChanging(self.pointer,self.PasOnChanging,oldobj,FreeOldEvent)
    def getOnChanging(self):
        return OnChangingcall
    OnChanging=property(getOnChanging,setOnChanging)
#class TCanvas end
#class TCustomIcon start
class TCustomIcon(TRasterImage):
#    pointer=c_void_p()
    def __init__(self):#TCustomIcon
        TRasterImage.__init__(self)
#constructorGraphics_TCustomIcon_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TCustomIcon_Create(),TCustomIcon)
    def getCurrent(self):
        r=LCLBinding.get_Graphics_TCustomIcon_Current(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setCurrent(self,v):
        LCLBinding.set_Graphics_TCustomIcon_Current(self.pointer,v)
    Current=property(getCurrent,setCurrent)
    def getCount(self):
        r=LCLBinding.get_Graphics_TCustomIcon_Count(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    Count=property(getCount)
#class TCustomIcon end
#class TIcon start
class TIcon(TCustomIcon):
#    pointer=c_void_p()
    def __init__(self):#TIcon
        TCustomIcon.__init__(self)
#constructorGraphics_TIcon_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TIcon_Create(),TIcon)
#class TIcon end
#class TPortableNetworkGraphic start
class TPortableNetworkGraphic(TFPImageBitmap):
#    pointer=c_void_p()
    def __init__(self):#TPortableNetworkGraphic
        TFPImageBitmap.__init__(self)
#constructorGraphics_TPortableNetworkGraphic_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TPortableNetworkGraphic_Create(),TPortableNetworkGraphic)
#class TPortableNetworkGraphic end
#class TPortableAnyMapGraphic start
class TPortableAnyMapGraphic(TFPImageBitmap):
#    pointer=c_void_p()
    def __init__(self):#TPortableAnyMapGraphic
        TFPImageBitmap.__init__(self)
#constructorGraphics_TPortableAnyMapGraphic_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TPortableAnyMapGraphic_Create(),TPortableAnyMapGraphic)
#class TPortableAnyMapGraphic end
#class TBitmap start
class TBitmap(TFPImageBitmap):
#    pointer=c_void_p()
    def __init__(self):#TBitmap
        TFPImageBitmap.__init__(self)
#constructorGraphics_TBitmap_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TBitmap_Create(),TBitmap)
#class TBitmap end
#class TFont start
class TFont(TFPCustomFont):
#    pointer=c_void_p()
    def __init__(self):#TFont
        TFPCustomFont.__init__(self)
#constructorGraphics_TFont_Create
    @staticmethod
    def Create():
        return LCLBindingUtil.GetPytonObject(LCLBinding.Graphics_TFont_Create(),TFont)
    def getIsMonoSpace(self):
        r=LCLBinding.get_Graphics_TFont_IsMonoSpace(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    IsMonoSpace=property(getIsMonoSpace)
    def getCanUTF8(self):
        r=LCLBinding.get_Graphics_TFont_CanUTF8(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    CanUTF8=property(getCanUTF8)
    def getPixelsPerInch(self):
        r=LCLBinding.get_Graphics_TFont_PixelsPerInch(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setPixelsPerInch(self,v):
        LCLBinding.set_Graphics_TFont_PixelsPerInch(self.pointer,v)
    PixelsPerInch=property(getPixelsPerInch,setPixelsPerInch)
    def getHeight(self):
        r=LCLBinding.get_Graphics_TFont_Height(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setHeight(self,v):
        LCLBinding.set_Graphics_TFont_Height(self.pointer,v)
    Height=property(getHeight,setHeight)
    def getName(self):
        r=LCLBinding.get_Graphics_TFont_Name(self.pointer)
        return LCLBindingUtil.ConvertPascalstring(r)
    def setName(self,v):
        LCLBinding.set_Graphics_TFont_Name(self.pointer,v)
    Name=property(getName,setName)
    def getOrientation(self):
        r=LCLBinding.get_Graphics_TFont_Orientation(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setOrientation(self,v):
        LCLBinding.set_Graphics_TFont_Orientation(self.pointer,v)
    Orientation=property(getOrientation,setOrientation)
    def getPitch(self):
        r=LCLBinding.get_Graphics_TFont_Pitch(self.pointer)
        return r
    def setPitch(self,v):
        LCLBinding.set_Graphics_TFont_Pitch(self.pointer,v.pointer)
    Pitch=property(getPitch,setPitch)
    def getQuality(self):
        r=LCLBinding.get_Graphics_TFont_Quality(self.pointer)
        return r
    def setQuality(self,v):
        LCLBinding.set_Graphics_TFont_Quality(self.pointer,v.pointer)
    Quality=property(getQuality,setQuality)
    def getSize(self):
        r=LCLBinding.get_Graphics_TFont_Size(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    def setSize(self,v):
        LCLBinding.set_Graphics_TFont_Size(self.pointer,v)
    Size=property(getSize,setSize)
    def getStyle(self):
        r=LCLBinding.get_Graphics_TFont_Style(self.pointer)
        return r
    def setStyle(self,v):
        LCLBinding.set_Graphics_TFont_Style(self.pointer,v.pointer)
    Style=property(getStyle,setStyle)
#class TFont end