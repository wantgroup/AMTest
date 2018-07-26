const { Given, When, Then } = require('cucumber');
const assert = require('assert');
const { driver } = require('../support/web_driver');

Given(/^浏览到搜索网站 "([^"]*)"$/, async function(url) {
    await driver.get(url);
});