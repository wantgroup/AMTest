import os

class Tools(object):

    def getRootPath(self):
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
    main()