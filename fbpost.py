import requests
from bs4 import BeautifulSoup
import os, sys
import time

def posting(pesan, cookie):
    grup = ["2061337210794733", "3852835338111671", "2802808803133004", "portogelofficial", "2494641837214326", "2470170899976440", "2326054951009910", "2302194580056903", "2260286497534555", "2108474526141274"]

    for i in range(len(grup)):
        url = "https://mbasic.facebook.com/groups/"+grup[i]
        with requests.session() as ses_:
            halaman  = ses_.get(url, cookies=cookie).content
            sop = BeautifulSoup(halaman, "html.parser")
            form = sop.find("form", method="post")
            url_post = form["action"]
            payload = {}
            for warga in form:
                input = warga
                payload[input.get("name")] = input.get("value")
            
            payload.update({"xc_message": pesan,
                            "view_post": "Posting"
            })
            ses_.post("https://mbasic.facebook.com/"+url_post, cookies=cookie, data=payload)
            print(30*"-")
            print("Postingan : " + pesan + "\ntelah selesai di upload di: " + url)

def pesan():
    os.system("cls")
    pesan = input("Postingan : ")
    time.sleep(3)
    cookie = {"cookie": "sb=jtbaYH5lofiTFy_Cuey1bHxq; datr=jtbaYEnR_l1wQryaaDzClf6l; c_user=100025060763675; xs=46%3AUY1k8PxUJGiCbg%3A2%3A1673756328%3A-1%3A11067; fr=0apMcUQVxdNd63BX8.AWXiOo0a30zAHVErsK0-ko2u328.BjnFpj.s9.AAA.0.0.Bjw36o.AWWUmxo88_k; m_page_voice=100025060763675; usida=eyJ2ZXIiOjEsImlkIjoiQXJvaWVvdngzbnZ1MiIsInRpbWUiOjE2NzM3NTYzODN9; wd=1366x695"}
    posting(pesan, cookie)

pesan()