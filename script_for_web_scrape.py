import requests
from bs4 import BeautifulSoup
import lxml
import csv
import os  # Import the os module to check for file existence

def scrape_booking(url, filename):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        print('Connected to web ')
        html_content = response.text

        # Create soup object
        soup = BeautifulSoup(html_content, 'lxml')

        # Find hotel containers
        hotel_divs = soup.find_all('div', role="listitem")

        # Check if the CSV file already exists
        file_exists = os.path.isfile(f'{filename}.csv')

        # Open CSV file for appending data
        with open(f'{filename}.csv', 'a', newline='', encoding='utf-8') as file_csv:
            writer = csv.writer(file_csv)

            # Write CSV header only if the file does not exist
            if not file_exists:
                writer.writerow(['hotel_name', 'locality', 'price', 'rating', 'score', 'review', 'link'])

            # Extract and write data
            for hotel in hotel_divs:
                try:
                    hotel_name = hotel.find('div', class_="f6431b446c a15b38c233").text.strip()
                except AttributeError:
                    hotel_name = 'N/A'

                try:
                    location = hotel.find('span', class_="aee5343fdb def9bc142a").text.strip()
                except AttributeError:
                    location = 'N/A'

                try:
                    price = hotel.find('span', class_="f6431b446c fbfd7c1165 e84eb96b1f").text.strip()
                except AttributeError:
                    price = 'N/A'

                try:
                    rating = hotel.find('div', class_="a3b8729ab1 e6208ee469 cb2cbb3ccb").text.strip()
                except AttributeError:
                    rating = 'N/A'

                try:
                    score = hotel.find('div', class_="a3b8729ab1 d86cee9b25").text.strip().split(' ')[-1]
                except AttributeError:
                    score = 'N/A'

                try:
                    link = hotel.find('a', href=True).get('href')
                except AttributeError:
                    link = 'N/A'

                try:
                    review = hotel.find('div', class_="abf093bdfe f45d8e4c32 d935416c47").text.strip()
                except AttributeError:
                    review = 'N/A'

                writer.writerow([hotel_name, location, price, rating, score, review, link])

        print(f'Data saved to {filename}.csv')

    else:
        print(f'Failed to connect to {url}. Status code: {response.status_code}')


# Input loop for multiple URLs
while True:
    url = input("Enter Booking.com URL (or type 'exit' to stop): ").strip()
    if url.lower() == 'exit':
        break

    filename = input("Enter filename (without extension): ").strip()

    scrape_booking(url, filename)

print("Scraping completed.")
