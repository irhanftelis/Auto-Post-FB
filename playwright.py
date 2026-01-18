from playwright.sync_api import sync_playwright
import time
import os

os.system("cls" if os.name == "nt" else "clear")
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        context.add_cookies([{
            'name': 'c_user',
            'value': '100050394665203',
            'domain': '.facebook.com',
            'path': '/'}, {
            'name': 'xs',
            'value': '27%3AQ-QOBXUX7bikHw%3A2%3A1768656085%3A-1%3A-1%3A%3AAcw-Si9ldauHKwjo_33DZC6RnesbobdntpqZ4wxQGg',
            'domain': '.facebook.com',
            'path': '/'
            }])

        page = context.new_page()
        page.goto("https://facebook.com/")
        
        global jumlah_comment
        while jumlah_comment > 0:
            jumlah_comment -= 1
            # buka ketik komentar
            page.locator('xpath=/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[4]/div/div[2]/div[1]/div/span/div/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[4]/div/div/div/div/div[2]/div/div[2]/div').click()
            time.sleep(2)
            #menulis komentar
            page.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/form/div/div[1]/div[1]/div/div[1]/div/div[1]').fill(komentar)
            #mengirim komentar
            page.locator('xpath=/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/form/div/div[2]/div/div[2]/div/div/div/span/div/div').click()


            print("Komentar berhasil dikirim!")
            print(page.title())
            time.sleep(10)
            page.reload()

jumlah_comment = int(input("Masukkan jumlah komentar yang diinginkan  : "))
komentar = input("Masukkan komentar yang diinginkan         : ")
main()