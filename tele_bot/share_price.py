from selenium import webdriver
import os

def get_quote(bot, update):
    message = update.message.text
    check_for_scrip_name = message.split(" ")

    if len(check_for_scrip_name) == 1:
        # We received only command, secutiry name was not sent. Send a error.
        bot.send_message(chat_id=update.message.chat_id, text="Security name was not sent. Send the command again with a security name.")

    else:
        # We received security name, take price from google and send

        security_name = " ".join(message.split(" ")[1:])

        chrome_driver = os.environ["WEBDRIVER.CHROME.DRIVER"]
        driver = webdriver.Chrome(chrome_driver)
        driver.get("https://www.google.co.in/search?q={} {}".format(security_name, "share price"))

        try:
            value = (driver.find_element_by_class_name("_FOc").text).encode("ascii", "ignore")
            bot.send_message(chat_id=update.message.chat_id, text=value)
        except:
            bot.send_message(chat_id=update.message.chat_id,
                             text="Error occured. Try again")
            #driver.quit()

        driver.quit()