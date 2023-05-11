import argparse
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

from Config import Config
from Exceptions.UnSatisfiedNumException import UnsatisfiedNumException


def init() -> tuple[str,Config]:
    parser = argparse.ArgumentParser(description='这样启动程序好处是可以命令行指定配置文件位置')
    parser.add_argument('-c', '--config', dest="configPath", default="./config/config.yaml")
    parser.add_argument('-u', '--url',dest="urlText",default="./config/url.txt")
    args = parser.parse_args()

    config = Config(args.configPath)
    url = args.urlText
    return url, config


def main(urlpath: str,config: Config):
    urls = []
    with open(urlpath, 'r', encoding='utf-8') as f:
        list = f.readlines()
        pattern = '(http|ftp|https)://[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-@?^=%&~\+#])?'
        for line in list:
            result = re.search(pattern,line)
            if result is not None:
                print(result.group())
                urls.append(result.group())

    accounts = config.accounts
    usernamelist = []
    passwordlist = []


    for account in accounts:
        username = accounts[account]["username"]
        password = accounts[account]["password"]
        usernamelist.append(username)
        passwordlist.append(password)

    if len(urls) != len(usernamelist):
        raise UnsatisfiedNumException

    weboption = webdriver.ChromeOptions()
    weboption.add_experimental_option("detach", True)
    weboption.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36')
    driver = webdriver.Chrome(options=weboption)

    begin = 'window.open("{}");'
    for index, url in enumerate(urls):
        js = begin.format(url)
        print(js)
        driver.execute_script(js)
        # driver.close()
        driver.switch_to.window(driver.window_handles[index+1])

        # handles = driver.window_handles
        # current_window = driver.current_window_handle
        # for handle in handles:
        #     if handle != driver.current_window_handle:
        #         driver.switch_to.window(handle)
        #         break
        '//*[@id="layui-layer100001"]/div[3]/a'
        '//*[@id="layui-layer1"]/div[3]/a'
        '//*[@id="layui-layer1"]/div[3]/a'
        '//*[@id="layui-layer100001"]/div[3]/a'
        '//*[@id="layui-layer100001"]/div[3]/a'
        popup_window1 = driver.find_elements(By.XPATH, '//*[@id="layui-layer100001"]/div[3]/a')
        if len(popup_window1) != 0:
            popup_window1[0].click()

        popup_window = driver.find_elements(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a')
        if len(popup_window) != 0:
            popup_window[0].click()

        Riotname = driver.find_element(By.XPATH,'//*[@id="CNsteamUser"]')
        print(Riotname)
        Riotpass = driver.find_element(By.XPATH,'//*[@id="CNsteampassword"]')
        Riotname.send_keys(usernamelist[index])
        Riotpass.send_keys(passwordlist[index])

        driver.find_element(By.XPATH,'//*[@id="centerdiv"]/div/div[1]/form/div[6]/div/button').click()
    # driver.quit()


if __name__ == '__main__':
    url,config = init()
    main(url,config)


