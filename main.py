import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pathlib
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("debuggerAddress", "localhost:8797")
scriptDirectory = pathlib.Path().absolute()
# scriptDirectory = pathlib.PurePath("../driver")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-web-security")
# chrome_options.add_argument("--headless")

chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument('--profile-directory=Profile 8')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
# TODO: We have to solve the userdata problem it have to in one directory
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")

service = Service(executable_path="C:\\Users\\user\\PycharmProjects\\BasicGoogleContact\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://basis.org.bd/company-profile/03-09-017")
driver.implicitly_wait(10)
time.sleep(1)

contact_x_path = "//div[@class='card-body pt-0']"
contact_elements = driver.find_element(By.XPATH, contact_x_path)
contact_text = contact_elements.text
print(contact_text)

print("\n..........................")

footer_address_xpath = "//div[@class='footer-address']"
footer_address_elements = driver.find_element(By.XPATH, footer_address_xpath)
footer_address_text = footer_address_elements.text
print(footer_address_text)

input("Stop ..:")
driver.get("https://contacts.google.com/")
email_xpath = "//input[@id='identifierId']"
driver.find_element(By.XPATH, email_xpath).send_keys("sushenbiswasaga")

input("Stop ..:")
