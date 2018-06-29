import csv
import time
import subprocess
import os
import re
import threading

switch=''
def LaunchAppCPU():
    "cpu使用情况命令"
    cmd = 'adb shell dumpsys cpuinfo | grep com.youdao.dict'
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    content = out.stdout.read()
    return content

def monkeyApp():
    "monkey"
    print(5)
    time.sleep(10   )
    print(4)
    cmd = 'adb shell monkey -p com.youdao.dict --throttle 120 200'
    subprocess.call(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(3)

def setAppCPUSC(switch):
    "读取曝使用情况信息"
    switch = switch
    while True:
        if switch==1:
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
            switch=2
        else:
            print(2)
            time.sleep(1)
            switch=1

def saveDataToCsv(fileName,alldata):
    '写入csv'
    fileCSV=None
    if(os.path.exists(fileName)):
        fileCSV = open(fileName, 'a',encoding="utf-8")
        alldata.pop(0)
    else:
        fileCSV = open(fileName, 'w', encoding="utf-8")

    writer = csv.writer(fileCSV)
    writer.writerows(alldata)

if __name__=="__main__":
    threads = []
    T1=threading.Thread(target=monkeyApp)
    T2=threading.Thread(target=setAppCPUSC,args=(1,))
    threads.append(T1)
    threads.append(T2)
    for t in threads:
        print(t)
        t.run()