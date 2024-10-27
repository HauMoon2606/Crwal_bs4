from bs4 import BeautifulSoup
import requests
import re

root = "https://subslikescript.com"
website = f"{root}/movies"
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content,"lxml")
box = soup.find("article",class_="main-article")
links =[]
for link in box.find_all("a",href = True):
    links.append(link["href"])

for link in links:
    web = f"{root}/{link}"
    result = requests.get(web)
    content = result.text
    soup = BeautifulSoup(content, "lxml")
    box = soup.find("article",class_ ="main-article")
    title = box.find('h1').get_text()
    title = title.split('-')[0]
    safe_title = re.sub(r'[\\/*?:"<>|]', "", title)
    transcript = box.find('div',class_= "full-script").get_text(strip=True, separator=" ")
    try:
        with open( f"{safe_title}.txt","w",encoding="utf-8") as file:
            file.write(transcript)
    except Exception as e:
        print(f"failed {e}")

