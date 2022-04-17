import requests
from bs4 import BeautifulSoup

htmldata = requests.get("https://www.rt.com/news/553925-west-want-war-moscow/") 
soup = BeautifulSoup(htmldata.text, 'html.parser') 
data = '' 
for data in soup.find_all("p"): 
    print(data.get_text()) 