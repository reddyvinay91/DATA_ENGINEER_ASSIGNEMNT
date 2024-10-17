from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Initialize the Chrome driver
service = Service('C:\\Users\\gully\\Data_engineer_assignemt\\chromedriver.exe')  # Update this path
driver = webdriver.Chrome(service=service)

# Navigate to the Amazon product search page
driver.get('https://www.amazon.com/s?k=laptops')  # You can change the search query

# Wait for the page to load
time.sleep(2)

# Extract product names and prices
products = driver.find_elements(By.XPATH, '//div[contains(@data-component-type,"s-search-result")]')

product_data = []

for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'h2 .a-link-normal').text
        price = product.find_element(By.CSS_SELECTOR, '.a-price-whole').text
        product_data.append({'name': name, 'price': price})
    except Exception as e:
        print(f"Error extracting product details: {e}")

# Close the driver
driver.quit()

# Convert extracted data to a DataFrame
df = pd.DataFrame(product_data)

# Clean data (if necessary)
df['price'] = df['price'].replace({',':''}, regex=True).astype(float)

# Save to CSV
df.to_csv('amazon_products.csv', index=False)

# Optionally save to SQLite
from sqlalchemy import create_engine
engine = create_engine('sqlite:///amazon_products.db')
df.to_sql('products', con=engine, if_exists='replace', index=False)

print("Data extraction complete. Check amazon_products.csv for results.")
