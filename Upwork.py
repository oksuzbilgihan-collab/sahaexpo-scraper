import os
os.system("cls")   # Windows
from bs4 import BeautifulSoup
import requests
import pandas as pd

liste = []
kapp = 1
for page in range(1,64git init):

    def decode_cfemail(cfemail):
        r = int(cfemail[:2], 16)

        email = ''.join(
            chr(int(cfemail[i:i+2], 16) ^ r)
            for i in range(2, len(cfemail), 2)
        )

        return email

    response = requests.get(f"https://sahaexpo.com/en/exhibitors?page={page}")
    soup = BeautifulSoup(response.content,"lxml")
    l1 = soup.find_all("a",class_="exhibitor-card")

    for i in l1 :
        linkler = i.get("href")
        # print(linkler)

        b = i.find_all("div",class_="exhibitor-card-content")
        for l in b :
            name = l.find("h3",class_="exhibitor-card-name").text.strip()
            # print(name)   
            ülke = l.find("div",class_="exhibitor-card-country").text.strip()
            # print(ülke)
            konum = l.find_all("div",class_="exhibitor-card-location")
            for k1 in konum:
                konum = l.find_all("div", class_="exhibitor-card-location")

                for k1 in konum:
                    deneme = k1.find("font")

                    if deneme:
                        konum1 = deneme.text.strip()
                    else:
                        konum1 = k1.text.strip()

                    # print(konum1)

        response1 = requests.get(linkler)
        soup1 = BeautifulSoup(response1.content,"lxml")
        kutu = soup1.find_all("div",class_="exhibitor-contact-list")
        mail_tag = soup1.find("span", class_="__cf_email__")

        if mail_tag:
            sifreli_mail = mail_tag.get("data-cfemail")

            gercek_mail = decode_cfemail(sifreli_mail)

            # print(gercek_mail)
        # for için in kutu :
        #     deneme1 = için.find("font")

            # if deneme1 :
            #     mail = deneme1.text.strip()
            #     print(mail)
            # else :
            #     mail = için.text.strip()
        kart = soup1.find("div",class_="exhibitor-categories-sidebar")
        sektör1 = []
        if kart :
            kartlar = kart.find_all("span",class_="exhibitor-category-tag-sm") 
            if kartlar :
                for karlar in kartlar :
                    sektör = karlar.text.strip()
                    if sektör :
                        sektör1.append(sektör)

        liste.append([name,linkler,ülke,gercek_mail,konum1,sektör1])
    print(f"\n{kapp} oldu ------------------------------------------------------------ ")
    kapp = kapp + 1


df = pd.DataFrame(liste)
df .columns=["Firma_ismi","Firma linki","Ülke","Mail_adresi","Konumu","Sektörü"]
print(df)
df.to_excel("upwork.xlsx")




