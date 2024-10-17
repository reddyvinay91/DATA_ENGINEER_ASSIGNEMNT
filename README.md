# Amazon Product Scraper

## Project Description
This project is a data pipeline that extracts product details from Amazon's search results page for laptops. It uses Selenium for web scraping, processes the data using Pandas, and stores it in a CSV file and a SQLite database.

## Technologies Used
- Python
- Selenium
- Pandas
- SQLite

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/USERNAME/REPOSITORY.git
Navigate to the project directory:
bash
Copy code
cd amazon_product_scraper
Install the required libraries:
bash
Copy code
pip install selenium pandas sqlalchemy
Usage
Make sure to have Chrome and ChromeDriver installed.
Run the script:
bash
Copy code
python scrape_amazon.py
Check the output files: amazon_products.csv and amazon_products.db.
Features
Extracts product names and prices from Amazon.
Saves data in both CSV and SQLite formats.
Handles dynamic web elements with error handling.
Challenges Faced
One of the main challenges was navigating the dynamic structure of the Amazon webpage, which required careful selection of CSS selectors to extract the desired data. Implementing error handling was crucial to prevent the script from crashing due to missing elements.

Future Improvements
Implement pagination to scrape multiple pages of results.
Enhance the data cleaning process for better quality data.
Add a user interface for easier interaction with the script.
License
This project is licensed under the MIT License.

Contact Information
Reddy Sri Vinay
reddysrivinayofficial@gmail.com



