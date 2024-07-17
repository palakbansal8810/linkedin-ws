import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')

user_input_job_title = input('Enter name\n').split()
username=input("enter your gmail id\n")
password=input("enter your password\n")
# Set up the Chrome webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.linkedin.com/login')

# Enter username and password and click login
driver.find_element(By.ID, "username").send_keys(username)  # Enter your username
driver.find_element(By.ID, "password").send_keys(password)  # Enter your password
driver.find_element(By.XPATH, "//*[@type='submit']").click()

job_title = '%2C%20'.join(user_input_job_title)

link = f"https://www.linkedin.com/search/results/people/?keywords={job_title}&origin=CLUSTER_EXPANSION&sid=s1B"

# Define the number of pages to scrape
num_pages = 3

# Create empty lists to store data
person_name = []
person_images = []
job_titles = []
location = []

for page_no in range(1, num_pages + 1):
    # Append page number to the search URL
    search_url = f"{link}&page={page_no}"
    
    # Navigate to the search URL
    driver.get(search_url)
    driver.implicitly_wait(10)
    
    # Scroll down to load more results
    for _ in range(2):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    
    # Extract data from the current page
    try:
        # Extract person names
        companies = driver.find_elements(By.XPATH, '//span[@dir="ltr"]//span[@aria-hidden="true"]')
        for person in companies:
            person_name.append(person.text)

        # Extract person images
        image_elements = driver.find_elements(By.CSS_SELECTOR, 'div.presence-entity.presence-entity--size-3 img')
        for image_element in image_elements:
            src = image_element.get_attribute('src')
            person_images.append(src)

        # Extract job titles
        titles = driver.find_elements(By.CSS_SELECTOR, 'div.entity-result__primary-subtitle.t-14.t-black.t-normal')
        for title in titles:
            job_titles.append(title.text)

        # Extract locations
        locs = driver.find_elements(By.CSS_SELECTOR, 'div.entity-result__secondary-subtitle.t-14.t-normal')
        for loc in locs:
            location.append(loc.text)
            
    except Exception as e:
        print("Error:", e)

# Ensure all lists have the same length
length = min_length = min(len(person_name), len(job_titles), len(person_images), len(location))

# Create a DataFrame using dictionary comprehension
df = pd.DataFrame({
    'Person Name': person_name[:length],  
    'Job Title': job_titles[:length],
    'Person Image': person_images[:length],
    'Location': location[:length]
})

print(df)

df.to_csv('linkedin_data.csv', index=False)
