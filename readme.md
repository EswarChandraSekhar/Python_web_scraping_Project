# 🏨 Booking.com Hotel Data Scraper

This project is a web scraping tool that extracts hotel data from **Booking.com**. It collects information such as hotel names, prices, locations, reviews, ratings, and direct booking links. The extracted data is cleaned and saved in a CSV file for further analysis.

## 📊 Example Outcome
| Hotel Name               | Price (INR) | Location         | Review        | No. of Ratings | Booking Link |
|--------------------------|-------------|------------------|---------------|----------------|--------------|
| The Taj Mahal Palace     | 25,000      | Mumbai           | Fabulous      | 5,421          | [Link](https://example.com) |
| ITC Grand Chola          | 18,500      | Chennai          | Excellent     | 4,893          | [Link](https://example.com) |
| The Oberoi Udaivilas     | 50,000      | Udaipur          | Exceptional   | 3,210          | [Link](https://example.com) |
| JW Marriott Sahar       | 22,000      | Mumbai           | Very Good     | 6,781          | [Link](https://example.com) |
| Hyatt Regency Delhi     | 15,000      | Delhi            | Good          | 3,528          | [Link](https://example.com) |

## 📂 Project Structure
```
web_scrape_project/
├── data/                     # CSV files with extracted and cleaned data
├── script_for_web_scrape.py  # Main web scraping script
├── requirements.txt          # Required packages
└── README.md                 # Project documentation
```

## 🛠️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/EswarChandraSekhar/booking-scraper.git
cd booking-scraper
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Scraper
```bash
python script_for_web_scrape.py
```
The extracted data will be saved as a CSV file in the `data/` directory.

## 📧 Author
**Eswar Chandra Sekhar**

- GitHub: [EswarChandraSekhar](https://github.com/EswarChandraSekhar)
- Email: eswaryadav9492@gmail.com

Feel free to contribute or reach out if you have any questions or suggestions!

