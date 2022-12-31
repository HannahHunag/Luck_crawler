from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
url = "https://www.luke54.org/index.php?option=com_jumi&view=application&fileid=41&cat=testimony"
options = Options()
browser = webdriver.Chrome()

for i in range(0, 7):
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    title_tag_list = soup.select('div[class="item-title"]')
    for title_tag_obt in title_tag_list:
        title_name = title_tag_obt.select_one('a').text
        print(title_name)
    #　next page
    page_nexts = browser.find_element(By.XPATH, '//*[@id="outer-page"]/div/span[4]')
    # 匯入 javascript
    browser.execute_script("arguments[0].click();", page_nexts)
    print("==============")
    time.sleep(0.75)
browser.close()
