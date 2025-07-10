import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests
from collections import Counter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import re

# Create Scrrenshot folders
os.makedirs("screenshots", exist_ok=True)
os.makedirs("cover_images", exist_ok=True)

WEBSITE_LINK = "https://elpais.com/"
OPINION_TAB_XPATH = "//a[@cmp-ltrk='portada_menu'][normalize-space()='Opinión']"
ARTICLES_XPATH = "//article[.//h2[contains(@class, 'c_t') and .//a]]"
TITLE_XPATH = ".//h2[contains(@class, 'c_t')]/a"

#Set options
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)


def take_screenshot(name):
    '''Method to take screenshot'''

    path = f"screenshots/{name}.png"
    driver.save_screenshot(path)
    print(f"[+] Screenshot saved: {path}")


def translate_text(text, from_lang="es", to_lang="en"):
    '''Method to make the API requiest'''

    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": "rapid-translate-multi-traduction.p.rapidapi.com",
        "x-rapidapi-key": "119e4fb11cmshe88fec1ccd77330p11ca6ajsn1bde26409440"
    }
    payload = {
        "from": from_lang,
        "to": to_lang,
        "q": text
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return result[0]
    except Exception as e:
        print(f"[-] Translation failed: {e}")
        return text  # will return original text if it fails



driver.get(WEBSITE_LINK)
time.sleep(3)
take_screenshot("homepage")

try:
    wait = WebDriverWait(driver, 10)
    opinion_tab = wait.until(EC.element_to_be_clickable(
        (By.XPATH, OPINION_TAB_XPATH)
    ))
    opinion_tab.click()
    time.sleep(3)
    take_screenshot("opinion_page")

except Exception as e:
    print(f"Failed to open opinion page: {e}")
    executor_object = {
    'action': 'setSessionStatus',
    'arguments': {
        'status': "<passed/failed>",
        'reason': "<reason>"
    }
}
browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
driver.execute_script(browserstack_executor)


# Get the link and title of top five articles
translated_titles = []
article_links = []
titles = []

articles = driver.find_elements(By.XPATH, ARTICLES_XPATH)[:5]
for article in articles:
    try:
        title_elem = article.find_element(By.XPATH, TITLE_XPATH)
        titles.append(title_elem.text.strip())
        article_links.append(title_elem.get_attribute("href").strip())
    except:
        continue


# Print the Title - URL - Content - Save_Cover_Image - Translated_Title 
for idx, (title, url) in enumerate(zip(titles, article_links), 1):
    try:
        print(f"\n--- Article {idx} ---")
        print("Title (ES):", title)
        print("URL:", url)

        driver.get(url)
        time.sleep(2)
        take_screenshot(f"03_article_{idx}_opened")

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        paragraphs = soup.select("div.a_c.clearfix[data-dtm-region='articulo_cuerpo'] p")
        content = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        # Trimming the content for better readability of output :)
        print("Content (ES):", content[:300], "...")

        img_tag = soup.select_one("figure img")
        if img_tag and img_tag.get("src"):
            img_url = img_tag.get("src")
            img_data = requests.get(img_url).content
            with open(f"cover_images/article_{idx}.jpg", "wb") as f:
                f.write(img_data)
            print(f"Image saved: cover_images/article_{idx}.jpg")

        translated = translate_text(title, from_lang="es", to_lang="en")
        translated_titles.append(translated+" hello")
        print("Title (EN):", translated)

        driver.back()
        time.sleep(2)

    except Exception as e:
        print(f"[-] Failed to process article {idx}: {e}")



print("\n--- Repeated Words in Translated Titles (more than 2 times) ---")
all_titles_text = " ".join(translated_titles)
words = re.findall(r'\b\w+\b', all_titles_text.lower())
word_counts = Counter(words)
no_words = True

for word, count in word_counts.items():
    if count > 2:
        print(f"{word}: {count}")
        no_words = False

if no_words:
    print("No Repeated Words in Translated Titles (more than 2 times)")

driver.quit()
