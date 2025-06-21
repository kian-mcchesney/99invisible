import xml.etree.ElementTree as ET
import pprint
import requests
from google import genai
from dotenv import load_dotenv
import os 

from bs4 import BeautifulSoup
# I used this link https://stackoverflow.com/questions/62002418/sitemap-xml-parsing-in-python-3-x


def init_gemini():
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEM_API_KEY")
    client = genai.Client(api_key=GEMINI_API_KEY)
    return client

def extractAuthorTitle(client,text):
    text=text
    prompt = f"""
    You are to get the author/journalist/writer's name and book title from this text snippet. Do not include any extra text or info. Format it so it is like 
    Author : 
    Title : 

    Here is the text snipped : 
    {text}

        """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    response=response.text.strip()
    authors=[]
    titles=[]
    #Each book is seperated by \n\n, creates a list
    books=response.split("\n\n")
    for i in books: 
        book_split=i.split("\n")
        author_split=book_split[0]
        title_split=book_split[1]
        author=author_split.removeprefix("Author :")
        title=title_split.removeprefix("Title :")
        authors.append(author.strip())
        titles.append(title.strip())
    return authors, titles


def getUrls(start,end):
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

    #only get certain urls for testing purposes 
    keys = list(episode_data.keys())[start:end]

    #gets urls and prints to double check


    for key in keys:
        link=episode_data[key]["url"]

        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
        }

        resp = requests.get(link, headers=headers)
        print(link)

       

#prints out text of article


def getEpisodeNumber(soup):
    episode_divs = soup.find_all("h4", class_=["entry-label", "post-label"])
    return episode_divs[0].text

def getBookInformation(soup):
    article_div = soup.find("main", class_="main")  
    text = article_div.get_text(separator=" ", strip=True)
    words=text.split()
    keywords = ["book", "books", "author", "authors"]
    window = 20
    contexts = []
    for i, word in enumerate(words):
        if word.lower() in keywords:
            start = max(i - window, 0)
            end = min(i + window + 1, len(words))
            context = words[start:end]
            contexts.append(" ".join(context))
    combined_context = "\n".join(contexts)

    return combined_context




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }

resp = requests.get("https://99percentinvisible.org/episode/tom-swift-electric-rifle/", headers=headers)

soup = BeautifulSoup(resp.content, "html.parser")

# episode=getEpisodeNumber(soup)
# print(episode)
# text=getBookInformation(soup)
# client=init_gemini()
# authors, titles=extractAuthorTitle(client,text)
# print(authors)
# print(titles)
getUrls(0,2)

