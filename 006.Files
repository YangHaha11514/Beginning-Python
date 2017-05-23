#打开或创建文件对象：
#file_object=open(file_name,access_mode='r',bufferinng=-1)
========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
#open()函数返回文件对象。 Open file and return a stream
    
#文件方法
read(self, size=-1, /)——读取给定字节数，默认-1代表读取至行结束符
readline(self, size=-1, /)—— 

f=open('D:\somefile.txt','r+'),r或r+模式下才能使用readline方法。
w模式下，会先清除文件中的信息

write(self, text, /)——返回写入的字符数
r+模式下，write方法会按写入文本长度一点一点覆盖原有文本

seek(self, cookie, whence=0, /)
 
for eachLine in f:
for eachLine in f.readline():
