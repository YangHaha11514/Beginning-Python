#类似于dir(list),help(zip)的获取语句关键词的详细信息的语句

#if语句：if本身，判断结果真假的条件表达式（and，or，not实现多重判断条件），表达式为真或非零时执行的代码块
#if...elif（0个或1个或多个）...else
#多个elif语句，可用1、序列和成员关系操作简化，2、字典，搜索快速
#三元操作符：x if C else y(C为真或非零，执行x,否则y)

#while语句：条件为真时循环执行代码块
#计数循环和无限循环

#for语句：
for iter_var in iterable:
    suite_to_repeat
#用于序列：序列项迭代，序列索引迭代，项和索引同时迭代（enumerate（））
#用于迭代器类型：
rang(start,end,step),xrang(start,end,step) #前者生成列表，后者生成可迭代对象（Python2，非序列非迭代器）
sorted（），zip（）#返回列表
reversed(),enumerate()#返回迭代器

#break语句：外部条件触发（一般if语句检查），从整个循环中退出。多层循环，最内部break,结束最内层循环！！！
#可用于while和for循环

#continue语句：终止当前循环，并忽略剩余的语句，然后回到循环的顶端。多层循环，最内部continue,返回最内层循环起始！！！
#pass语句

#else语句可以在while和for循环中使用，循环完成后执行

#迭代器:next()方法的对象。不能先后移动，不能回到开始，也不能复制（反过来，如何实现？？）
#两种调用方法：for...in...表达式和iter()-next()流程
#迭代序列：i=iter(sequence)-next(i)
#迭代字典：i=iter(dict/dict.keys()),i=iter(dict.values()),i=iter(dict.items())-next(i)通过键、值、键值对迭代dict
#迭代文件：for eachLine in myFile自动调用readline()方法，or for eachLine in myFile.readlines()
#可变对象和迭代器：迭代可变对象时尽量不修改它们！！如需修改，使用副本！！

#列表解析：[expr for iter_var in iterable if con]
#可以替代map()和filter()函数：map(lamda x:expr(x),iterable)

#生成器表达式：（expr for iter_var in iterable if con）

#itertools模块
