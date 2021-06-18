import time
import sys
from selenium import webdriver

email = sys.argv[1]
first_name = sys.argv[2]
last_name = sys.argv[3]
password = sys.argv[4]

#Sites
websites = {
    "BigW": "https://www.bigw.com.au/product/playstation-5-console/p/124625/",
    "Amazon": "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945/ref=sr_1_1?crid=IIP48EJJKL34&dchild=1&keywords=playstation+5&qid=1623918489&s=videogames&sprefix=play%2Caps%2C355&sr=1-1",}


buy_button = False
ps5_acquired = False

def amazon_buy():
    try:
        browser.get(websites["Amazon"])
        try:
            buy_now_button = browser.find_element_by_id("buy-now-button")
            buy_now_button.click()
        except:
            time.sleep(3)
            browser.close()

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
        time.sleep(1)
        ps5_acquired = True
        browser.close()
    except:
        pass


def bigw_buy():
    
while not ps5_acquired:
    browser = webdriver.Firefox()
    amazon_buy()
    print("scanning")
