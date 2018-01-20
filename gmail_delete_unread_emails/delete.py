from selenium import webdriver
import os
import time

chrome_driver = os.environ["WEBDRIVER.CHROME.DRIVER"]
driver = webdriver.Chrome(chrome_driver)
driver.get("https://gmail.com")
raw_input("Login and press enter : ")


# target the inverted triangle

try:
    driver.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-Pm T-I-ax7 L3 J-JN-M-I']").click()
    menu = driver.find_element_by_xpath("//div[@id=':30']//div[@class='J-J5-Ji J-JN-M-I-JG']")
except:
    menu = driver.find_element_by_xpath("//div[@id=':2r']//div[@class='J-J5-Ji J-JN-M-I-JG']")
next_page = driver.find_elements_by_xpath("//div[@id=':io']")

while True:
    menu.click()

    unread = driver.find_element_by_xpath("//div[@class='J-N']")
    print "unread click"
    unread.click()
    """//div[@class='J-J5-Ji J-JN-M-I-Jm']"""
    # delete icon appears only after selecting mails, so doing this op here.

    check_status = ""
    try
    #T-Jo J-J5-Ji T-Jo-auq T-Jo-aMF
    #T-Jo J-J5-Ji T-Jo-auq T-Jo-Jp
    selected = driver.find_element_by_xpath("//span[@class='T-Jo J-J5-Ji T-Jo-auq T-Jo-ayH']") #aria-checked

    if selected.get_attribute("aria-checked") == "mixed":
        delete = driver.find_element_by_xpath("//div[@class='asa']")
        delete.click()
    else:
        next_page.click()

    time.sleep(1)
