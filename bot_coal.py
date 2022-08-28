from selenium import webdriver as wd
import time
import random

window = wd.Chrome("C:/chromedriver.exe")
window.implicitly_wait(10)


window.get("https://sklep.pgg.pl/")
random_wait_time = random.randrange(5.0,10.0)
time.sleep(random_wait_time)


add_to_cart=window.find_element("xpath","/html/body/div[1]/section/div/div/div[7]/div[6]/form/button/i")
add_to_cart.click()
time.sleep(random_wait_time)



