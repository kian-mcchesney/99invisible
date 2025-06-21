from google import genai
from dotenv import load_dotenv
import os 

load_dotenv()
# use ai to extract the title and author
GEMINI_API_KEY = os.getenv("GEM_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
text=f{input_text}

prompt = f"""
You are to get the author/journalist/writer's name and book title from this text snippet. Format it so it is like 
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
print(response)

#example set up to see if dictionary works 

#Lists to store authors and titles
authors=[]
titles=[]
#Each book is seperated by \n\n, creates a list
books=response.split("\n\n")

print(len(books))
for i in books: 
    book_split=i.split("\n")
    author_split=book_split[0]
    title_split=book_split[1]
    author=author_split.removeprefix("Author :")
    title=title_split.removeprefix("Title :")
    authors.append(author.strip())
    titles.append(title.strip())

print(authors)
print(titles)




def getBookInfo(text,url):

