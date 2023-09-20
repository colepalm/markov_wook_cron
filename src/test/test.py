import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# Set up a wait
wait = WebDriverWait(driver, timeout=10)


# Function to generate the post using an HTTP request
def generate_post():
    response = requests.get('https://wookmark.fly.dev/generate')
    if response.status_code == 200:
        return response.text
    else:
        raise Exception('Failed to generate post')


# Open the website and perform actions
try:
    # Generate post using the generate_post function
    wook_post = generate_post()

    # Direct to the main phish page
    driver.get('https://phantasytour.com/bands/phish/threads')
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hide_overflow')))

    # Login
    driver.find_element(By.XPATH, "//*[contains(text(), 'Log in')]").click()
    wait.until(EC.presence_of_element_located((By.ID, 'login_username')))
    driver.find_element(By.ID, 'login_username').send_keys('wook_mark')
    driver.find_element(By.ID, 'login_password').send_keys('4iZ!83vZ')
    driver.find_element(By.CLASS_NAME, 'btn-secondary').click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'hide_overflow')))

    # Find thread
    elements = driver.find_elements(By.CLASS_NAME, 'hide_overflow')
    elements[10].click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'post_body_container')))

    # Enter wook post
    driver.find_element(By.CLASS_NAME, 'form-control').send_keys(wook_post)

    # Submit wook post
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()

except Exception as e:
    print(e)
finally:
    # Close the WebDriver
    driver.quit()
