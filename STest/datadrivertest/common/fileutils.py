import os
import platform
import datetime
import inspect
import base64
from HTMLReport import AddImage
from common import driver_uilts

#获取当前运行路径
def NowPath():
    return os.getcwd()
#获取上级路径
def superiorPath():
    return os.path.abspath(os.path.dirname(os.getcwd()))
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
#传入文件路径进行创建文件夹
def setMakedirs(path):
    if os.path.exists(path):
        return path
    else:
        os.makedirs(path)
        return path
#截屏存放路径
def screenShotPath():
    path=superiorPath()
    path = path+getSystem()+'screenshots'+getSystem()+getYear()+getSystem()+getMouth()+getSystem()+getDay()
    return setMakedirs(path)
#测试报告存放路径
def reportPath():
    path = superiorPath()
    path = path + getSystem() + 'report' + getSystem() + getYear() + getSystem() + getMouth() + getSystem() + getDay()
    return setMakedirs(path)
#获取当前运行的方法名
def getFunctionName():
    return inspect.stack()[1][3]
#存放HTMLReport的测试报告img的函数
def addReportImg(drivar):
    data=driver_uilts.getScreenShotData(drivar)
    image = base64.b64encode(data)
    AddImage(image)
if __name__ == "__main__":
    print(screenShotPath())