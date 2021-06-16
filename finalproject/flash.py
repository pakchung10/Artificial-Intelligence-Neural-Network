from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()  # 需要 下载 对应浏览器 驱动到 python 安装目录
driver.get("http://wxmz.gzthfy.com/?v=2021060101159#/ReportList")  # 刷新网址

for i in range(10000):  # 刷新次数
    driver.refresh()  # 刷新网页
    sleep(10)  # 五秒一次