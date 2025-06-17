from google import genai
from dotenv import load_dotenv
import os 
load_dotenv()

# use ai to extract the title and author
GEMINI_API_KEY = os.getenv("GEM_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
# text="""
# Host Roman Mars spoke with Kassia St. Clair, author of The Secret Lives of Color. This episode was produced by Emmett Fitzgerald


# re at 99% Invisible, we think about color a lot, so it was really exciting when we came across a beautiful book called The Secret Lives of Color by Kassia St. Clair. It’s this amazing collection of stories about different colors, the way they’ve been made through history, 
# """

text="""
Producer Kurt Kohlstedt spoke with Norman Brosterman, author of Inventing Kindergarten; Tamar Zinguer, author of Architecture in Play: Intimations of Modernism in Architectural Toys; and Alexandra Lange, author of The Design of Childhood: How the Material World Shapes Independent Kids.


"""

prompt = f"""
You are to get the author and book title from this text snippet. Format it so it is like 
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

url="https://99percentinvisible.org/episode/the-secret-lives-of-color/"
episode_number=0 
date = ""


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



