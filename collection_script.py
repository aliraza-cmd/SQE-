from bs4 import BeautifulSoup
import os
import pandas as pd


d = {'title' : [], 'price' : [], 'link' : []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("div", class_="RfADt")
        title = t.get_text()
        finaltitle = " ".join(title.split())
        p = soup.find("span", class_="ooOxS")
        price = p.get_text()
        l = t.find("a")
        link = "https:"+l['href']
        
        
        d['title'].append(finaltitle)
        d['price'].append(price)
        d['link'].append(link)
    except Exception as e:
        print(e)

df = pd.DataFrame(data=d)
df.to_csv("data.csv")




# print(price)

# print(f"{" ".join(title.split())}", link, price)
# t = soup.find_all("a", "title")
# title = t.get_text()
# print(a)

