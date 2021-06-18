import time
import sys
from selenium import webdriver

email = sys.argv[1]
first_name = sys.argv[2]
last_name = sys.argv[3]
password = sys.argv[4]

# https://www.bigw.com.au/product/playstation-5-console/p/124625/
#
#Sites
websites = {
    "BigW": "https://www.bigw.com.au/product/ps5-pulse-3d-gaming-headset/p/124629/",
    "Amazon": "https://www.amazon.com.au/PlayStation-5-Console/dp/B08HHV8945/ref=sr_1_1?crid=IIP48EJJKL34&dchild=1&keywords=playstation+5&qid=1623918489&s=videogames&sprefix=play%2Caps%2C355&sr=1-1",
    "Sony": ""}


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

        add_to_cart = browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/main/div/div[1]/div[2]/div[8]/div[1]/button[1]")
        add_to_cart.click()

        postcode = browser.find_element_by_xpath("html.aem-AuthorLayer-Edit.noscroll body.page.basicpage.ReactModal__Body--open div.ReactModalPortal div.ReactModal__Overlay.ReactModal__Overlay--after-open.ModalOverlay div.ReactModal__Content.ReactModal__Content--after-open.Modal.size-small.SetUserLocationModal div.modal-content div.SetUserLocationModalContent div.input-container div.SuburbInput.css-2b097c-container div.SuburbInputPrefix__control.css-yk16xz-control div.SuburbInputPrefix__value-container.css-1hwfws3 div.css-1g6gooi div.SuburbInputPrefix__input input#react-select-3-input")
        postcode.click()
        postcode.send_keys(4212)
        postcode.send_keys("\n")
        return True
    except:
        time.sleep(1)
        #browser.close()
        return True

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
    print("###scanning### AMAZON -- ps5_aquired: " + str(ps5_acquired))
    ps5_acquired = amazon_buy(ps5_acquired)
    #print("###scanning### BIGW -- ps5_aquired: " + str(ps5_acquired))
    #ps5_acquired = bigw_buy(ps5_acquired)
    # print("###scanning### SONY -- ps5_aquired: " + str(ps5_acquired))
    # ps5_acquired = bigw_buy(ps5_acquired)
