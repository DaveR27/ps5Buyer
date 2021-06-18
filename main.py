import time
import sys
from selenium import webdriver

email = sys.argv[1]
first_name = sys.argv[2]
last_name = sys.argv[3]
password = sys.argv[4]

# https://www.bigw.com.au/product/playstation-5-console/p/124625/
#Sites
websites = {
    "BigW": "https://www.bigw.com.au/product/playstation-5-hd-camera/p/124631/",
    "Amazon": "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945/ref=sr_1_1?crid=IIP48EJJKL34&dchild=1&keywords=playstation+5&qid=1623918489&s=videogames&sprefix=play%2Caps%2C355&sr=1-1",}


buy_button = False
ps5_acquired = False

def amazon_buy(acquired):
    browser = webdriver.Firefox()
    try:
        browser.get(websites["Amazon"])
        buy_now_button = browser.find_element_by_id("buy-now-button")
        buy_now_button.click()

        email_input = browser.find_element_by_id("ap_email")
        email_input.click()
        email_input.send_keys(email)

        email_continue = browser.find_element_by_id("continue")
        email_continue.click()

        password_input = browser.find_element_by_id("ap_password")
        password_input.click()
        password_input.send_keys(password)

        password_continue = browser.find_element_by_id("signInSubmit")
        password_continue.click()

        place_your_order_button = browser.find_element_by_name("placeYourOrder1")
        place_your_order_button.click()
        time.sleep(10)
        browser.close()
        return True
    except:
        time.sleep(1)
        browser.close()
        return False


def bigw_buy(acquired):
    browser = webdriver.Firefox()
    try:
        browser.get(websites["BigW"])

        button = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/div/div[1]/div[2]/div[8]/div[1]/button[1]")
        button.click()
        return True
    except:
        time.sleep(1)
        #browser.close()
        return True

while not ps5_acquired:
    print("###scanning### AMAZON -- ps5_aquired: " + str(ps5_acquired))
    #ps5_acquired = amazon_buy(ps5_acquired)
    print("###scanning### BIGW -- ps5_aquired: " + str(ps5_acquired))
    ps5_acquired = bigw_buy(ps5_acquired)
