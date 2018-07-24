let wd=require('wd')
let path=require('path')

async function run(){
    let driver = await wd.promiseChainRemote({
        host: '127.0.0.1',
        port: 4723
      });
    let desiredCaps = {
    platformName: 'IOS',
    platformVersion: '11.4',
    deviceName: 'iPhone 8 Plus',
    app: path.resolve('/Users/cloudin/Library/Developer/Xcode/DerivedData/订餐-dcxvdcqhqbbrdmgauarbdoihzkgj/Build/Products/Debug-iphonesimulator/订餐.app')
    };
    driver.init(desiredCaps);
}
run()
  
  