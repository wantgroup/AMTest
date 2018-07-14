#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

class Tools(object):

    def getRootPath(self):
        '''
        获取上级目录的路径
        :return:
        '''
        rootpath = os.path.dirname(os.path.abspath(__file__))
        while rootpath:
            if os.path.exists(os.path.join(rootpath, 'readme.md')):
                break
            rootpath = rootpath[0:rootpath.rfind(os.path.sep)]

        return rootpath


def main():
    tools = Tools()
    rootpath = tools.getRootPath()
    apkpath = os.path.join(rootpath,'apks','cnode.apk')
    print(apkpath)

if __name__ == '__main__':
    d=Tools().getRootPath()
    print(d)
    main()