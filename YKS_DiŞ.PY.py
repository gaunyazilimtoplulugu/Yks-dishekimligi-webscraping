import requests
from bs4 import BeautifulSoup 

class Scraping():
    def __init__(self):
        self.url_dis = "https://www.universitego.com/dis-hekimligi-2021-taban-puanlari-ve-basari-siralamalari/"
    def web_scraping(self):
        html = requests.get(self.url_dis).content
        soup = BeautifulSoup(html,"html.parser")
        return soup.find('tbody').find_all("tr")
scrap = Scraping()

while True:
    secim = input("1--Tüm Diş Hekimliği Sıralamaları\n2--Sıralamama Gelen Diş Hekimliği Fakülteleri\n3--Exit\nSeçiminiz:")
    print('-'*50)
    if secim=="3":
        break
    else:
        if secim=="1":
            result = scrap.web_scraping()
            for a in result:
                if a.find_all('td')[5].string=='Başarı Sırası':
                    pass
                else:
                    print(f"OKUL ADI:{a.find_all('td')[0].string}---------SIRALAMA:{a.find_all('td')[5].string}---------KONTENJAN:{a.find_all('td')[3].string}")
        elif secim == "2":
            siralama = float(input("Sıralamanızı giriniz: "))
            c = scrap.web_scraping()
            print("SIRALAMANIZA GELEN ÜNİVERSİTELER".center(100,"*"))
            for b in c:
                x = b.find_all('td')[5].string
                if x=='Başarı Sırası':
                    continue
                elif float(x)<=siralama:
                    print('-'*100)
                    print(f"OKUL ADI:{b.find_all('td')[0].string}---------SIRALAMA:{b.find_all('td')[5].string}---------KONTENJAN:{b.find_all('td')[3].string}")
                    
