import os
import time
import requests
import re
from collections import Counter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


#---------------------- CONSTANTS ----------------------
WEBSITE_LINK = "https://elpais.com/"
COOKIE_ACCEPT_BUTTON = "didomi-notice-agree-button"
OPINION_TAB_XPATH = "//a[@cmp-ltrk='portada_menu'][normalize-space()='Opinión']"
ARTICLES_XPATH = "//article[.//h2[contains(@class, 'c_t') and .//a]]"
TITLE_XPATH = ".//h2[contains(@class, 'c_t')]/a"

#---------------------- Setup ----------------------
os.makedirs("screenshots", exist_ok=True)
os.makedirs("cover_images", exist_ok=True)

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 60)

def take_screenshot(name):
    path = f"screenshots/{name}.png"
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")

# ---------------------- Visit El País ----------------------
try:
    driver.get(WEBSITE_LINK)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    # Handle cookie/TC notification popup if it appears
    try:
        accept_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, COOKIE_ACCEPT_BUTTON))
        )
        accept_button.click()
        print("Accepted cookie banner")
    except:
        print("Cookie banner not found or already accepted")

    take_screenshot("homepage")
except Exception as e:
    print("Failed to load homepage:", e)
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"name": "Failed_Test_Run", "status":"failed", "reason": "Failed to load homepage"}}')
    driver.quit()
    exit()

# Navigate to Opinión section using provided XPath
try:
    opinion_tab = wait.until(EC.element_to_be_clickable((By.XPATH, OPINION_TAB_XPATH)))
    opinion_tab.click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    take_screenshot("opinion_section")
except Exception as e:
    print("Could not locate 'Opinión' tab via XPath:", e)
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"name": "Failed_Test_Run", "status":"failed", "reason": "Could not locate Opinión tab via XPath"}}')
    driver.quit()
    exit()

# ---------------------- Collect Article Titles and Links ----------------------
translated_titles = []
article_links = []
titles = []

try:
    articles = driver.find_elements(By.XPATH, ARTICLES_XPATH)[:5]
    for article in articles:
        title_elem = article.find_element(By.XPATH, TITLE_XPATH)
        titles.append(title_elem.text.strip())
        article_links.append(title_elem.get_attribute("href").strip())
except Exception as e:
    print("Failed to extract articles:", e)
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"name": "Failed_Test_Run", "status":"failed", "reason": "Failed to extract articles"}}')
    driver.quit()
    exit()

# ---------------------- Translation Function ----------------------
def translate_text(text, from_lang="es", to_lang="en"):
    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": "rapid-translate-multi-traduction.p.rapidapi.com",
        "x-rapidapi-key": "*"
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
        if isinstance(result, list) and len(result) > 0:
            return result[0]
        else:
            return text
    except Exception as e:
        print(f"Translation failed: {e}")
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"name": "Failed_Test_Run", "status":"failed", "reason": "Failed to translate"}}')
        driver.quit()
        exit()

# ---------------------- Process Each Article ----------------------
for idx, (title, url) in enumerate(zip(titles, article_links), 1):
    try:
        print(f"\n--- Article {idx} ---")
        print("Title (ES):", title)
        print("URL:", url)

        driver.get(url)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        take_screenshot(f"article_{idx}_opened")

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        paragraphs = soup.select("div.a_styled-content p")
        if not paragraphs:
            paragraphs = soup.select("div.a_c.clearfix[data-dtm-region='articulo_cuerpo'] p")

        content = "\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        print("Content (ES):", content[:300], "...") # Trimming the content of article for better readability of log :)
    
        img_tag = soup.select_one("figure img")
        if img_tag and img_tag.get("src"):
            img_url = img_tag.get("src")
            img_data = requests.get(img_url).content
            with open(f"cover_images/article_{idx}.jpg", "wb") as f:
                f.write(img_data)
            print(f"Image saved: cover_images/article_{idx}.jpg")

        translated = translate_text(title, from_lang="es", to_lang="en")
        translated_titles.append(translated)
        print("Title (EN):", translated)

        driver.back()
        time.sleep(2)

    except Exception as e:
        print(f"Failed to process article {idx}: {e}")
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"name": "Failed_Test_Run", "status":"failed", "reason": "Failed to process article"}}')
        driver.quit()
        exit()

# ---------------------- Analyze Translated Titles ----------------------
print("\n--- Repeated Words in Translated Titles (more than 2 times) ---")
try:
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

except Exception as e:
    print("Failed during word analysis:", e)
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"name": "Failed_Test_Run", "status":"failed", "reason": "Failed during word analysis"}}')
    driver.quit()
    exit()
    

#Everything works good marking session as passed
driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"name": "Successful_Test_Run", "status":"passed", "reason": "Everything Worked Fine!"}}')
driver.quit()
