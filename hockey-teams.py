import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.scrapethissite.com/pages/forms/'
sabres_history = []

response =  requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
pagination = soup.find('ul', class_='pagination')
page_numbers = [int(link.text.strip()) for link in pagination.find_all('li') if link.text.strip().isdigit()]
last_page = max(page_numbers)

print(f"Starting to scrape {last_page} pages...")

for page in range(1, last_page + 1):
    page_url = f"{url}?page_num={page}"
    print(f"Checking page {page}...")

    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for row in soup.find_all('tr', class_='team'):
        team_name = row.find('td', class_='name').text.strip()
        if team_name == 'Buffalo Sabres':
            year = row.find('td', class_='year').text.strip()
            wins =  row.find('td',class_='wins').text.strip()
            losses = row.find('td', class_='losses').text.strip()

            print(f"Found Sabres Year {year}, Wins: {wins}, Losses: {losses}")

            if not any(season['year'] == year for season in sabres_history):
                sabres_history.append({
                    'year': year,
                    'wins': int(wins),
                    'losses': int(losses)
                })
    time.sleep(1)

print("\nFinal Results:")
for season in sorted(sabres_history, key=lambda x: x['year']):
    print(f"Year: {season['year']}, Wins: {season['wins']}, Losses: {season['losses']}")
print(f"\nTotal unique seasons collected: {len(sabres_history)}")