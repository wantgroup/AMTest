import csv
import time
import subprocess
import os
import re
import threading

def LaunchApp():
    "使用命令启动app"
    cmd = 'adb shell am start -W -n com.youdao.dict/.activity.DictSplashActivity'
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    content = out.stdout.read()
    return content

def LaunchAppCPU():
    "cpu使用情况命令"
    cmd = 'adb shell dumpsys cpuinfo | grep com.youdao.dict'
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    content = out.stdout.read()
    return content

def monkeyApp():
    "monkey"
    cmd = 'adb shell monkey -p com.youdao.dict 200'
    subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

def setAppCPUSC():
    "读取曝使用情况信息"
    content=LaunchAppCPU()
    o = bytes.decode(content)
    s = o.split('\n')
    alldata = [('当前时间', 'cpu使用率')]
    startTime = ""
    for item in s:
        match=re.compile("(.*?)"+"/com.youdao.dict:"+".*?")
        startTime=re.findall(match,item)
        startTime=''.join(startTime)
        match=re.compile("  "+"(.*?)"+"% "+".*?")
        startTime=re.findall(match,startTime)
        startTime=''.join(startTime)
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        str(startTime)
        if ''!=startTime:
            alldata.append((currentTime,startTime+"%"))
        print(alldata)
    fileName='cpu.csv'
    saveDataToCsv(fileName, alldata)

def setAppStartTimeCSV():
    "读取启动时间"
    content=LaunchApp()
    o = bytes.decode(content)
    s = o.split('\n')
    startTime = ''
    alldata = [('当前时间', '启动时间')]
    for item in s:
        if item.find('ThisTime') > -1:
            item = item.replace('\r', ' ')
            startTime = item.split(":")[1]
            startTime = int(startTime.strip())
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    alldata.append((currentTime, startTime))
    fileName='some.csv'
    saveDataToCsv(fileName,alldata)

def saveDataToCsv(fileName,alldata):
    fileCSV=None
    if(os.path.exists(fileName)):
        fileCSV = open(fileName, 'a',encoding="utf-8")
        alldata.pop(0)
    else:
        fileCSV = open(fileName, 'w', encoding="utf-8")

    writer = csv.writer(fileCSV)
    writer.writerows(alldata)

if __name__=="__main__":
    pass