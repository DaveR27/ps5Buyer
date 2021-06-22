import time
import sys
import os
from selenium import webdriver

first_name = sys.argv[1]
last_name = sys.argv[2]
email = sys.argv[3]
postcode_in = sys.argv[4]
password = sys.argv[5]
csv = sys.argv[6]

#Sites
websites = {
    "BigW": "https://www.bigw.com.au/product/playstation-5-console/p/124625/",
    "Amazon": "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945/ref=sr_1_1?crid=IIP48EJJKL34&dchild=1&keywords=playstation+5&qid=1623918489&s=videogames&sprefix=play%2Caps%2C355&sr=1-1",
    "Sony": ""
}

testWebsites = {
    "BigW": "https://www.bigw.com.au/product/playstation-4-500gb-slim-console-jet-black/p/531009/",
    "Amazon": "https://www.amazon.com.au/PlayStation-4-500GB-Console-Black/dp/B0773RV962/ref=sr_1_1?crid=10U5ENL6A4AMJ&dchild=1&keywords=playstation+4&qid=1624163824&sprefix=playstation+4%2Caps%2C318&sr=8-1",
    "Sony": ""
}

mode = websites
buy_button = False
ps5_acquired = False

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()

def amazon_buy(acquired):
    browser = webdriver.Firefox(options=fireFoxOptions)
    try:
        browser.get(mode["Amazon"])

        time.sleep(2)
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

        time.sleep(3)
        place_your_order_button = browser.find_element_by_xpath('/html/body/div[5]/div/div[2]/div[2]/div/div[2]/div[1]/form/div[2]/div/div/div/span/span/input')
        if mode == websites:
            place_your_order_button.click()
        print("We got it !!!!!!!!")
        return True
    except:
        time.sleep(2)
        browser.close()
        return False


def bigw_buy(acquired):
    browser = webdriver.Firefox(options=fireFoxOptions)
    try:
        browser.get(mode["BigW"])

        add_to_cart = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/div/div[1]/div[2]/div[8]/div[1]/button[1]')
        add_to_cart.click()

        time.sleep(1)
        postcode = browser.find_element_by_xpath('/html/body/div[10]/div/div/div/div/div/div/div')
        postcode.click()
        time.sleep(1)
        postcode_enter = browser.find_element_by_id('react-select-2-input')
        postcode_enter.send_keys(postcode_in)
        time.sleep(1)
        postcode_enter.send_keys(webdriver.common.keys.Keys.ENTER)

        time.sleep(1)
        save_button = browser.find_element_by_xpath('/html/body/div[10]/div/div/div/div/div[3]/button')
        save_button.click()
        
        time.sleep(1)
        add_to_cart2 = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/div/div[1]/div[2]/div[8]/div/div[1]/div[3]/button[1]')
        add_to_cart2.click()

        checkout = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/header/div[2]/div[2]/button[2]')
        checkout.click()

        time.sleep(1)

        procced_to_checkout = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/div[2]/div/div[2]/section/div[5]/button')
        procced_to_checkout.click()

        time.sleep(1)
        email_input = browser.find_element_by_id('login__email')
        email_input.click()
        email_input.send_keys(email)

        password_input = browser.find_element_by_id('login__password')
        password_input.click()
        password_input.send_keys(password)

        login_button = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/main/div/div[1]/form/div[3]/button')
        login_button.click()

        time.sleep(2)
        procced_to_payment = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/section/section/form/div/div/button')
        procced_to_payment.click()

        time.sleep(5)

        credit_card = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/section/section/section[2]/div[2]/section/div[2]/header/section/input')
        credit_card.click()

        csv_input = browser.find_element_by_xpath('//*[@id="saved-cards__cv2"]')
        csv_input.click()
        csv_input.send_keys(csv)
        
        time.sleep(2)

        buy_button = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[3]/section/section/section[2]/div[2]/section/div[2]/section/div/form/div[3]/button')
        if mode == websites:
            buy_button.click()
        print("We got it !!!!!!!!")
        return True
    except:
        time.sleep(2)
        browser.close()
        return False

def sony_buy(acquired):
    browser = webdriver.Firefox()
    try:
        browser.get(websites["Sony"])

        
        return True
    except:
        time.sleep(1)
        browser.close()
        return False

while not ps5_acquired:
    print("###scanning### Amazon")
    ps5_acquired = amazon_buy(ps5_acquired)
    print("ps5_aquired: " + str(ps5_acquired))
    if ps5_acquired:
        break
    print("###scanning### BigW") 
    ps5_acquired = bigw_buy(ps5_acquired)
    print("ps5_aquired: " + str(ps5_acquired))
    if ps5_acquired:
        break
    # print("###scanning### SONY -- ps5_aquired: " + str(ps5_acquired))
    # ps5_acquired = bigw_buy(ps5_acquired)
    os.system("rm geckodriver.log")
    os.system("rm -rf /tmp/*")