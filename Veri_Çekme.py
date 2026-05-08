import os
os.system("cls")   # Windows
from bs4 import BeautifulSoup
import requests
import pandas as pd


response = requests.get("https://sahaexpo.com/en/exhibitors")
soup = BeautifulSoup(response.content,"lxml")
liste = []
l1 = soup.find_all("div",attrs={"class":"exhibitor-grid"})
for i in l1 :
    link1 = i.find_all("a",attrs={"class":"exhibitor-card"})
    for x in link1:
        link = x.get("href")
        liste.append(link)

        # print(link)
        response1 = requests.get(link)
        soup1 = BeautifulSoup(response1.content,"lxml")
        b1 = soup1.find_all("div",attrs={"class":"exhibitor-contact-list"})
        for b2 in b1 :
            b3 = b2.find_all("div",attrs={"class":"exhibitor-contact-item"})
            for b4 in b3 :
                bölge = b4.find("font",attrs={"dir":"auto"})
            #     print(b4.text.strip())
            # print("\n")
        m1 = soup1.find_all("a",attrs={"class":"exhibitor-contact-item exhibitor-contact-link"})
        for m2 in m1 :
            m3 = m2.find_all("font",attrs={"dir":"auto"})
            for m4 in m3 :
                m5 = m4.text.strip()
                print(m4) 
        