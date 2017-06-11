#类vs实例，类及实例的内建函数
#类属性vs实例属性
#类方法vs实例方法：创建、查看、调用、重构
#特殊方法：构造方法，一般的特殊方法；
#用特殊方法定制类
#多态、封装、继承



#类的创建：
class ClassName(bases):
    class_suite
#类属性
#类的方法：第一个参数必须为self，类不能直接调用方法，方法必须与实例绑定
#查看类属性：dir(ClassName),ClassName.__dict__ 
#特殊的类方法：C.__name__,C.__doc__,C.__bases__,C.__dict__,C.__module__,C.__class__
    
#实例化：1-初始化类mc=ClassName()，2-检测__init__方法
#构造器方法：__init__(),__new__()（标准类型的构造方法）;结构器：__del__()
class InstCt():
    count=0
    def __init__(self):
        InstCt.count+=1
    def __del__(self):
        InstCt.count-=1
    def howmany(self):
        return(InstCt.count)
#实例属性：__init__()中设置
#查看实例属性:dir();__dict__,var()
#特殊的实例方法：I.__class__;I.__dict__

#实例属性vs类属性
#类访问并更新类属性
#实例访问类属性（类属性不可变，类属性为词典等可变对象）

#实例属性只能通过类创建后，自定义实例属性？？？ 
#实例继承了所有的类属性，相当于copy了一份类属性，类属性与实例属性同名但不完全相同（背后的基础原理？？？）

#类MyClass及其实例mc,无法通过MyClass.foo()调用，可以mc.foo()调用。foo()方法绑定到了实例mc上
#调用非绑定方法：主要应用场景——派生子类，覆盖掉父类的构造方法，先调用父类的构造方法以重用代码
#可否用在覆盖普通的父类方法，先调用该父类方法以重用代码？？？？？

#组合；子类和派生
#重用基类的代码：调用未绑定的基类方法（普通方法或特殊方法-构造方法），或super()函数
class P(object):
    def __init__(self):
        print("Calling P's constructor")
    def foo(self):
        print("Hi,I'm P-foo")
        
class C(P):
    def __init__(self):
        P.__init__(self)#or super(C,self).__init__()
        print("Calling C's constructor")
    def foo(self):
        P.foo(self)#or super(C,self).foo()
        print("Hi,I'm C-foo")

#定制类
#1.从标准类中派生，或模拟标准类
#1.1.调用父类的构造方法
class RoundFloat(float):
    def __new__(cls,val):
        return(float.__new__(cls,round(val,2)))#or return(super(RoundFloat,cls).__new__(cls.round(val,2)))
#注意其中的构造函数为__new__(),及代表自身的关键词cls
#需要理解标准类的构造方法__new__()的定义及动作
#1.2.重写标准类的一般方法
class SortedKeyDict(dict):#重写dict的keys()方法
    def keys(self):
        return(sorted(super(SortedKeyDict,self).keys())#dict()创建词典的用法及各种方法，SortedKeyDict同样可以调用
#1.3.重写标准类的特殊方法
#实现序列或映射规则：__len__(self),__getitem__(self,key),__setitem__(self,key,value),__delitem__(self,key)
class RoundFloatManual(object):
    def __init__(self,val):
        assert isinstance(val,float),\
        'value must be a float'#输入参数必须为浮点数
        self.value=round(val,2)#返回两位小数    
    def __str__(self):#可以使用print函数表示
        return('%.2f'%self.value)
    __repr__=__str__#可以字符串对象表示，且和print结果相同

#1.4.迭代器规则：
class AnyIter(object):
    def __init__(self,data,safe=False):
        self.safe=safe
        self.iter=iter(data)
    def __iter__(self):
        return(self)
    def next(self,howmany=1):
        retval=[]
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return(retval)

#2.重载操作符
class Time60(object):
    def __init__(self,hr,min):
        self.hr=hr
        self.min=min
    def __str__(self):
        return('%d:%d'%(self.hr,self.min))
    __repr__=__str__
    def __add__(self,other):
        return(self.__class__(self.hr+other.hr,self.min+other.min))
    def __iadd__(self,other):
        self.hr+=other.hr
        self.min+=other.min
        return(self)
       
#3.多类型定制：
class NumStr(object):
    def __init__(self,num=0,string=''):
        self.__num=num
        self.__string=string
    def __str__(self):
        return('[%d::"%s"]'%(self.__num,self.__string))
    __repr__=__str__
    def __add__(self,other):
        if isinstance(other,NumStr):
            return(self.__class__(self.__num+other.__num,self.__string+other.__string))
        else:
            raise TypeError
    def __mul__(self,num):
        if isinstance(num,int):
            return(self.__class__(self.__num*num,self.__string*num))
        else:
            raise TypeError
    def __nonzero__(self):
        return(self.__num or len(self.__string))
    def __norm_cval(self,cmpres):
        return(cmp(cmpres,0))
    def __cmp__(self,other):
        return(self.__norm_cval(cmp(self.__num+other.__num))+self.__norm_cval(cmp(self.__string+other.__string)))

 
            

#多重继承，及其解析顺序？？？？？
    
#类、实例等内建函数：
#issubclass(sub,sup),isinstance(obj1,obj2)
#hasattr(),getattr(),setattr(),delattr()
#dir(),super(),var()

#私有化：双下划线（__）和单下划线（_）

#包装：对已存在的类型进行定制；授权：更新的功能由新类的某部分处理，已存在功能授权给对象的默认属性
#授权关键点在于覆盖__getattr__()方法，包含一个对getattr()内建函数的调用
class WrapMe(object):
    def __init__(self,obj):
        self.__data=obj
    def get(self):#删除包装并返回原始对象
        return(self.__data)
    def __repr__(self):
        return('self.__data)
    def __str__(self):
        return(str(self.__data))
    def __getattr__(self,attr):
        return(getattr(self.__data,attr))

from time import time,ctime        
class TimeWrapMe(object):
    def __init__(self,obj):
        self.__data=obj
        self.__ctime=self.__mtime=self.__atime=time()
    def get(self):
        self.__atime=time()
        return(self.__data)
    def gettimeval(self,t_type):
        if not isinstance(t_type,str) or t_type[0] not in 'cma':
            raise TypeError
        return(getattr(self,'_%s__%stime'%(self.__class__.__name__,t_type[0])))
    def set(self,obj):
        self.__data=obj
        self.__mtime=self.__atime=time()
    def __repr__(self):
        self.__atime=time()
        return('self.__data')
    def __str__(self):
        self.__atime=time()
        return(str(self.__data))
    def __getattr__(self,attr):
        self.__atime=time()
        return(getattr(self.__data,attr))
        
        
        
        
        
        
    




#新式类的高级特性
#__slots__类属性：
#__getattribute__特殊方法：
#描述符descriptors:包含__get__(),__set__(),__delete__()三者中至少一个，三者充当描述符协议的作用
#没有__set__()方法为非数据描述符，同时__set__(),__get__()数据描述符
#def __get__(self,obj,type=None)->value;def __set__(self,obj,val)->None;def __del__(self,obj)->None






#静态方法和类方法？？？？？？？
1.普通方法必须以实例作为第一个参数，通常命名为self
2.classmethod，以类本身作为第一个参数，通常命名为cls
3.staticmethod，不需要类或实例作为第一个参数

class Demo():
    def normmeth(*args):
		return(args)
        
    @classmethod
    def klassmeth(*args):
        return(args)
        
    @staticmethod
    def statmeth(*args):
        return(args)

#分别通过实例和类调用三种方法
Demo().normmeth()#返回(<__main__.Demo object at 0x000001801332EF98>,)
Demo().normmeth('spam')#返回(<__main__.Demo object at 0x000001801332EF98>,'spam')

Demo.klassmeth()#返回(<class '__main__.Demo'>,)
Demo.klassmeth('spam')#返回(<class '__main__.Demo'>,'spam')
Demo().klassmeth()#返回(<class '__main__.Demo'>,)
Demo().klassmeth('spam')#返回(<class '__main__.Demo'>,'spam')

Demo.staticmeth()#返回空元组()
Demo.staticmeth('spam')#返回('spam',)
Demo().staticmeth()#返回空元组()
Demo().staticmeth('spam')#返回('spam',)


#相关模块



