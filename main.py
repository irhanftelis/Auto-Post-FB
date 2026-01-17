from selenium import webdriver
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import os
import time

os.system("cls" if os.name == "nt" else "clear")

def main():
    global driver
    #setup chrome driver
    option = webdriver.ChromeOptions()
    option.add_argument("--maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=option)


    # login facebook dengan cookie
    driver.get("https://www.facebook.com/")

    cookies = [ {"name": "c_user", "value": "100050394665203", "path": "/"}, {"name": "xs", "value": "27%3AQ-QOBXUX7bikHw%3A2%3A1768656085%3A-1%3A-1%3A%3AAczeQOG-HXLkg3eLgSM1CyRJvuOL54Q2zmrNzifRRQ", "path": "/"} ]
    for cookie in cookies: 
        driver.add_cookie(cookie)

    print(driver.title)
    driver.refresh()

#comment function
def comment():
    #komentar di postingan
    comment_box = WebDriverWait(driver, 10).until( EC.element_to_be_clickable(("xpath", "//span[contains(text(),'Komentari')]")) )
    driver.execute_script("arguments[0].scrollIntoView();", comment_box)
    driver.execute_script("arguments[0].click();", comment_box)
    time.sleep(2)

    #mengetik komentar
    comment_area = WebDriverWait(driver, 10).until( EC.element_to_be_clickable(("xpath", "//div[@role='textbox']")) ) 
    comment_area.send_keys(komen)

    #submit komentar
    post_button = driver.find_element("xpath", '//*[@id="focused-state-composer-submit"]/span/div/div')  
    driver.execute_script("arguments[0].click();", post_button)

    print("Komentar berhasil dikirim!")
    time.sleep(delay)  # jeda antara komentar
    driver.refresh()

# i = int(input("Masukkan jumlah komentar yang diinginkan: "))
komen = input("Masukkan komentar yang diinginkan: ")
jumlah_comment = int(input("Masukkan jumlah komentar yang diinginkan: "))
delay = int(input("Masukkan jeda waktu antar komentar (dalam detik): "))
main()
for _ in range(jumlah_comment):
    comment()