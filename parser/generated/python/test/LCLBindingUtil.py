POD=dict([(-1,0)])
def GetPytonObject2(key):
    print "key=",key
    return POD[key]
def GetPytonObject(key,T):
    try:
        return POD[key]
    except:
        POD[key]=T()
        POD[key].pointer=key
        return POD[key] 
def SetPytonObject(key,obj):
    print "key=",key
    POD[key]=obj
    
def ConvertPascalTCaption(c):
    return c
def ConvertPascalstring(c):
    return c
def ConvertPascalBoolean(b):
    if b==1:
        return True
    else:
        return False
def ConvertPascalInteger(i):
    return i
def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]]
def CreateSetFormint(i,SE):
    bf=bitfield(i)
    l=len(bf)
    k=0
    print "k=",k
    print bf
    bf.reverse()
    print bf
    s=set()
    jj=1
    k=0
    while k<l:
        bf[k]=bf[k]*pow(2,k)
        try:
            temp=bf[k]
            print "temp",temp
            s.add(SE[temp])
        except:
            jj=0
        k=k+1
    return s

    k=0
    while k>32:
        if k==1:
            s.add(SE[k])
        k=k+1
