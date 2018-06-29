import os
import time
import csv
import subprocess


class App(object):

    def __init__(self):
        self.content = ""
        self.startTime = 0
        
    def LaunchApp(self):
        cmd = 'adb shell am start -W -n com.youdao.dict/.activity.DictSplashActivity'
        out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.content = out.stdout.read()

    def StopApp(self):
        cmd = 'adb shell am force-stop com.youdao.dict/.activity.DictSplashActivity'
        out = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        out.stdout.read()

    def GetLaunchedTime(self):
        o = bytes.decode(self.content)
        s = o.split('\n')
        for item in s:
            if item.find('ThisTime') > -1 :
                item = item.replace('\r',' ')
                self.startTime = item.split(":")[1]
                self.startTime = int(self.startTime.strip())

        return self.startTime
    

class Controller(object):
    def __init__(self,counter):
        self.app = App()
        self.counter = counter
        self.alldata = [('当前时间','启动时间')]
    
    def testprocess(self):
        self.app.LaunchApp()
        elpasedtime = self.app.GetLaunchedTime()
        time.sleep(1)
        self.app.StopApp()
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime,elpasedtime))

    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime
    
    def run(self):
        while self.counter > 0:
            self.testprocess()
            # print("exec ",self.counter)
            self.counter = self.counter - 1
    
    def saveDataToCsv(self):
        with open('some.csv', 'w',encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(self.alldata)

if __name__ == '__main__':
    # controller = Controller(10)
    # controller.run()
    # controller.saveDataToCsv()
    s=1
    print("df %d"  % s)