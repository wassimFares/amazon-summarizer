from bs4 import BeautifulSoup
import requests
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
genai.configure(api_key = os.getenv('GENAI_API'))

model = genai.GenerativeModel('gemini-1.0-pro-latest')




def get_reviews(url, lang):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    comments = soup.find_all('div', {'class':'a-expander-content reviewText review-text-content a-expander-partial-collapse-content'})

    list = []
    i = 1
    for comment in comments:
        list.append(f"{i}- {comment.contents[1].text}")
        i += 1

    response = model.generate_content(f"Those are reviews on a product on amazon can you summarize them in {lang} one paragraph for positives and one for negatives for me?\n\n{list}\n\nPlease use this format\n\nPositives:\n-line1\nline2\n\nNegatives:\n-line1\nline2\n(No more characters Please and don't change anything on the format.)")

    print(response.text)
    return response.text

