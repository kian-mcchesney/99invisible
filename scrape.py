import xml.etree.ElementTree as ET
import pprint
import requests

from bs4 import BeautifulSoup
# I used this link https://stackoverflow.com/questions/62002418/sitemap-xml-parsing-in-python-3-x

episode_data={}

tree = ET.parse('episode-sitemap.xml')
root = tree.getroot()

#Add urls to a dictionary with transcript added to path
for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
    #print(loc+"transcript")
    episode_data[url]={

        "url": loc+"transcript",
        
    }
    #print(episode_data[url])

start = 10
end = 12

#only get certain urls for testing purposes 
keys = list(episode_data.keys())[start:end]

#gets urls and prints to double check
for key in keys:
    link=episode_data[key]["url"]

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }

    resp = requests.get(link, headers=headers)
    #print(resp)


#prints out text of article

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }

resp = requests.get("https://99percentinvisible.org/episode/611-ancient-dms", headers=headers)

soup = BeautifulSoup(resp.content, "html.parser")

print(soup.text)