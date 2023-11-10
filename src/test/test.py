import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 " \
             "Safari/537.36"
# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox=600000000')
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument('--disable-dev-shm-usage')  

width = 1920
height = 1080

chrome_options.add_argument(f"--window-size={width},{height}")

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# Set up a wait
wait = WebDriverWait(driver, timeout=300)


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
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'navbar-brand')))

    # Wait for the "Log in" link to be clickable
    print("Before waiting for the login button to be clickable.")

    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Log in')]")))
    print("After waiting for the login button to be clickable.")

    # Click the "Log in" link
    login_button.click()
    print("Clicked Log in link.")

    # Wait for the login_username element
    wait.until(EC.presence_of_element_located((By.ID, 'login_username')))
    print("Login page loaded successfully.")

    driver.find_element(By.ID, 'login_username').send_keys('wook_mark')
    driver.find_element(By.ID, 'login_password').send_keys('4iZ!83vZ')
    driver.find_element(By.CLASS_NAME, 'btn-secondary').click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'navbar-brand')))
    print("Login successful.")

    # Find the 10th row in the table
    tr_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//table[@class='thread-listing']/tbody/tr[10]")))
    print("Successfully clicked on the 10th row in the table.")

    # Find the <a> element inside the <tr>
    a_element = tr_element.find_element(By.TAG_NAME, "a")

    # Click the <a> element
    a_element.click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'post_body_container')))

    # Enter wook post
    driver.find_element(By.CLASS_NAME, 'form-control').send_keys(wook_post)

    # Submit wook post
    driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    print("Successfully clicked on the post creation button.")

    print('post created successfully')

except Exception as e:
    print(f"An error occurred: {e}")
    print(f"Exception class: {e.__class__}")

finally:
    # Close the WebDriver
    driver.quit()