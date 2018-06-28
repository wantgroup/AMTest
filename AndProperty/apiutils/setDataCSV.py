import csv
import time
import subprocess

def LaunchApp():
    cmd = 'adb shell am start -W -n com.youdao.dict/.activity.DictSplashActivity'
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    content = out.stdout.read()
    return content

def setAppStartTimeCSV():
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
    print(alldata)
    saveDataToCsv(alldata)

def saveDataToCsv(alldata):
    with open('some.csv', 'w',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(alldata)

if __name__=="__main__":
    setAppStartTimeCSV()