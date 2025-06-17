from google import genai


# use ai to extract the title and author
GEMINI_API_KEY = "AIzaSyDjFS5cdz_yJ1un_8ekUdEUHYiqNncr-F0"
client = genai.Client(api_key=GEMINI_API_KEY)
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

print(response.text.strip())


