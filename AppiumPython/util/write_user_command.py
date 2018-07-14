# coding=utf-8
import yaml
import os
import sys
sys.path.append('/Users/cloudin/Desktop/project/AMTest/AppiumPython')

from util.tools import Tools

tool = Tools()
rootpath = tool.getRootPath()
yaml_path = os.path.join(rootpath, 'config', 'userconfig1.yaml')

class WriteUserCommand:
    def read_data(self):
        '''
        加载yaml数据
        '''
        print(yaml_path)
        with open(yaml_path) as fr:
            data = yaml.load(fr)
        return data

    def get_value(self, key, port):
        '''
        获取value
        '''
        data = self.read_data()
        value = data[key][port]
        return value

    def write_data(self, i, device, bp, port):
        '''
        写入数据
        '''
        data = self.join_data(i, device, bp, port)
        with open(yaml_path, "a") as fr:
            yaml.dump(data, fr)

    def join_data(self, i, device, bp, port):
        data = {
            "user_info_" + str(i): {
                "deviceName": device,
                "bp": bp,
                "port": port
            }
        }
        return data

    def clear_data(self):
        with open(yaml_path, "w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        data = self.read_data()
        print(data)
        return len(data)


if __name__ == '__main__':
    write_file = WriteUserCommand()
    s=write_file.get_file_lines()
    print(s)
