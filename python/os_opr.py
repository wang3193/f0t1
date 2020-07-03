# 系统操作
import os

# 获取文件后缀名
file_ext = os.path.splitext('./data/py/test.py')
print(file_ext)
print(file_ext[1])

# 文件读取操作
def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.makedir(path)

'''
如果用默认open(filename)读取会使用系统默认编码gbk
'''
def openfile(filename):
    f = open(filename, 'r', encoding='utf-8')
    fllist = f.read()
    f.close()
    return fllist

print(openfile("c:/workspace/demo/f0t1/python/base.py"))

# 文件写操作
# 如果文件存在,则清空再写入,文件不存在创建
f = open(r"c:/file/tmp/test.txt", "w", encoding="utf-8")
f.write("hello world")
f.close

# a写入, 文件存在,在内容后追加写入,不存在则创建
f = open(r"c:/file/tmp/test2.txt", "a", encoding="utf-8")
f.write("hello world \n")
f.close

# 自动关闭文件和处理异常
with open(r"c:/file/tmp/test3.txt", "w") as f:
    f.write("Hello python")

# 路径文件名
file_ext = os.path.split('./data/tst/test.py')
print(file_ext)

