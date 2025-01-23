from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Set up WebDriver (Replace 'chromedriver' with the path to your driver)
driver_path = "path/to/chromedriver"
driver = webdriver.Chrome(driver_path)

def search_address_on_site(address):
try:
# Open the Find People Search website
driver.get("https://www.findpeoplesearch.com/")

# Locate the search box and input the address
search_box = driver.find_element(By.NAME, "q") # Replace 'q' with the actual search box name or ID
search_box.clear()
search_box.send_keys(address)
search_box.send_keys(Keys.RETURN)

time.sleep(3) # Wait for results to load (adjust as needed)

# Extract results (modify selectors based on the site's HTML structure)
try:
owner = driver.find_element(By.CSS_SELECTOR, ".owner-class").text # Replace with the actual selector
except:
owner = "Not Found"

try:
phone_number = driver.find_element(By.CSS_SELECTOR, ".phone-class").text # Replace with the actual selector
except:
phone_number = "Not Found"

return {"Owner": owner, "Phone Number": phone_number}
except Exception as e:
print(f"Error searching for address {address}: {e}")
return {"Owner": "Error", "Phone Number": "Error"}

def process_file(file_path):
data = pd.read_csv(file_path)
results = []

for index, row in data.iterrows():
address = row['Address'] # Ensure the file has an 'Address' column
print(f"Processing address: {address}")
result = search_address_on_site(address)
results.append({"Address": address, **result})

# Save results to a new file
output_file = "output_with_phone_numbers.csv"
pd.DataFrame(results).to_csv(output_file, index=False)
print(f"Results saved to {output_file}
