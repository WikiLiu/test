###一个带参数的test.py文件
import sys
import os

arg0 = sys.argv[0] # 为打包的exe
arg1 = sys.argv[1] #为exe在cmd运行的第一个参数

print(arg0)
print(arg1)
print(os.getcwd()+arg1)