from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
counter =0
while True:
    try:
        counter += 1
        driver = webdriver.Chrome(r"C:\chromedriver.exe",
                              options=chrome_options)
        driver.get("https://app.ex.co/stories/erezez10/2020-10-08t17-12-44-557z-")
        time.sleep(4)
        driver.execute_script("window.scrollTo(0, 3000)")
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[14]/div/div/div[1]/div[2]/div[2]/div/div/button").click()
        time.sleep(3)
        driver.close()
        driver.quit()
        print(counter)
    except :
        counter -= 1
