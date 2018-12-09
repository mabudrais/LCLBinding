from MainPasObject import *
#import end
#class TLCLComponent start
class TLCLComponent(TComponent):
#    pointer=c_void_p()
    def __init__(self):#TLCLComponent
        TComponent.__init__(self)
#constructorLCLClasses_TLCLComponent_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.LCLClasses_TLCLComponent_Create((TheOwner.pointer)),TLCLComponent)
    def getLCLRefCount(self):
        r=LCLBinding.get_LCLClasses_TLCLComponent_LCLRefCount(self.pointer)
        return LCLBindingUtil.ConvertPascalInteger(r)
    LCLRefCount=property(getLCLRefCount)
#class TLCLComponent end
#class TLCLReferenceComponent start
class TLCLReferenceComponent(TLCLComponent):
#    pointer=c_void_p()
    def __init__(self):#TLCLReferenceComponent
        TLCLComponent.__init__(self)
    def getHandleAllocated(self):
        r=LCLBinding.get_LCLClasses_TLCLReferenceComponent_HandleAllocated(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    HandleAllocated=property(getHandleAllocated)
    def getReferenceAllocated(self):
        r=LCLBinding.get_LCLClasses_TLCLReferenceComponent_ReferenceAllocated(self.pointer)
        return LCLBindingUtil.ConvertPascalBoolean(r)
    ReferenceAllocated=property(getReferenceAllocated)
#constructorLCLClasses_TLCLReferenceComponent_Create
    @staticmethod
    def Create(TheOwner):
        return LCLBindingUtil.GetPytonObject(LCLBinding.LCLClasses_TLCLReferenceComponent_Create((TheOwner.pointer)),TLCLReferenceComponent)
#class TLCLReferenceComponent end
