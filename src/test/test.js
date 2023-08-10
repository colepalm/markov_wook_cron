require('chromedriver');
const webdriver = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const { By, until } = webdriver;
const fetch = require('node-fetch')

const chai = require('chai');
const chaiAsPromised = require('chai-as-promised');

chai.use(chaiAsPromised);

const screen = {
  width: 1040,
  height: 680
};

const timeout = 99999999999999;

const options = new chrome.Options()

options.addArguments('--disable-dev-shm-usage')
options.addArguments('--no-sandbox')
options.addArguments('--headless')

const driver = new webdriver.Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();

describe('Make Wook Post', () => {
  before(async () => {
    try {
      await driver.manage().setTimeouts({
        implicit: timeout,
        pageLoad: timeout,
        script: timeout
      })
    } catch(err) {
        console.log(err)
      }
  });

  it('generate post', async () => {
    try {
      const res = await fetch('https://wookmark.fly.dev/generate');
      this.wookPost = await res.text()
    } catch (err) {
      console.log(err)
    }
  })

  it('Direct to main phish page', async () => {
    await driver.get('https://phantasytour.com/bands/phish/threads');
    await driver.wait(until.elementLocated(By.className('hide_overflow')));
  });

  it('Login', async () => {
    await driver.findElement(By.xpath("//*[contains(text(), 'Log in')]")).click();
    await driver.wait(until.elementLocated(By.id('login_username')));
    await driver.findElement(By.id('login_username')).sendKeys('wook_mark');
    await driver.findElement(By.id('login_password')).sendKeys('4iZ!83vZ');
    await driver.findElement(By.className('btn-secondary')).click();
    await driver.wait(until.elementLocated(By.className('hide_overflow')));
  });

  it('Find thread', async () => {
    const elements = await driver.findElements(By.className('hide_overflow'));
    await elements[10].click();
    await driver.wait(until.elementLocated(By.className('post_body_container')));
  });

  it('Enter wook post', async () => {
    await driver.findElement(By.className('form-control')).sendKeys(this.wookPost);
  });

  it('Submit wook post', async () => {
    await driver.findElement(By.className('btn-primary')).click();
  })
});
