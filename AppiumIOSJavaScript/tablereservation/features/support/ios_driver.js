let wd = require('wd');

//根据您的浏览器配置创建WebDriver实例;
function createDriver() {
    let driver = await wd.promiseChainRemote({
    host: '127.0.0.1',
    port: 4723
    });
    let desiredCaps = {
    platformName: 'IOS',
    platformVersion: '7.0',
    deviceName: 'Android Emulator',
    app: path.resolve('path', 'to', 'app.apk')
    };
    driver.init(desiredCaps);
    return driver;
}

exports.driver = createDriver();