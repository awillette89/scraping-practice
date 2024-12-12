import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

countries_data = []

countries = soup.find_all('div', class_='country')

for country in countries:
    country_info = {
        'name': country.find('h3', class_='country-name').text.strip(),
        'capital': country.find('span', class_='country-capital').text,
        'population': country.find('span', class_='country-population').text
    }
    countries_data.append(country_info)
    
for country in countries_data[:5]:
    print(country)

total_countries = len(countries)
print(f"Total number of countries: {total_countries}")