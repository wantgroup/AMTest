import os
import platform
import datetime

#创建目录
def makedirectory(filePath):
    if  os.path.exists(filePath):
        return filePath
    else:
        os.makedirs(filePath)
        return filePath

#处理不同系统下斜杠的问题
def getSystem():
    System=platform.system()
    if 'Windows' == System:
        return '\\'
    else:
        return '/'
#获取当前年 月 日 时 分
def getYear():
    return str(datetime.datetime.now().year)
def getMouth():
    return  str(datetime.datetime.now().month)
def getDay():
    return  str(datetime.datetime.now().day)
def getHour():
    return str(datetime.datetime.now().hour)
def getMinute():
    return str(datetime.datetime.now().minute)
#获取上级路径
def superiorPath():
    return os.path.abspath(os.path.dirname(os.getcwd()))
#测试报告存放路径
def reportPath():
    return makedirectory(superiorPath() + getSystem() + 'test_result' + getSystem() + getYear() + getSystem() + getMouth() + getSystem() + getDay())
