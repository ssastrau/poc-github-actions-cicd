import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url = f"https://{sys.argv[1]}ip.linodeusercontent.com/"
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
driver.get(url)
title = driver.title.lower()
driver.quit()
if "Jenkins" not in title:
    print("Jenkins is not started")
    sys.exit(1)
print("Jenkins is started")
