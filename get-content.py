import requests
from bs4 import BeautifulSoup

# Define the URLs of the websites to scrape
urls = ['https://www.bbc.co.uk/learningenglish/', 
        'https://www.englishcentral.com/',
        'https://www.englishpage.com/']

# Loop through the URLs and scrape the content
for url in urls:
    # Send a GET request to the website and get the HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the relevant content from the HTML
    if url == 'https://www.bbc.co.uk/learningenglish/':
        # Get the latest news headlines and descriptions
        news_headlines = soup.find_all('div', {'class': 'gel-1/2@l'})
        for headline in news_headlines:
            title = headline.h3.text.strip()
            description = headline.p.text.strip()
            print(f'Title: {title}\nDescription: {description}\n')
    elif url == 'https://www.englishcentral.com/':
        # Get the latest video lessons
        video_lessons = soup.find_all('div', {'class': 'slider-item'})
        for lesson in video_lessons:
            title = lesson.find('h3').text.strip()
            description = lesson.find('p').text.strip()
            print(f'Title: {title}\nDescription: {description}\n')
    elif url == 'https://www.englishpage.com/':
        # Get the latest grammar lessons
        grammar_lessons = soup.find_all('div', {'class': 'block'})
        for lesson in grammar_lessons:
            title = lesson.h2.text.strip()
            description = lesson.p.text.strip()
            print(f'Title: {title}\nDescription: {description}\n')