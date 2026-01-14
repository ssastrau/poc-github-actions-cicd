import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = f"https://{sys.argv[1]}.ip.linodeusercontent.com/"
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
try:
    driver.get(url)
    title = driver.title.lower()
finally:
    driver.quit()
if "Jenkins" not in title:
    print("Jenkins is not started")
    sys.exit(1)
print("Jenkins is started")