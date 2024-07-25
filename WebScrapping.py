from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from bs4 import BeautifulSoup
import time

def setup_driver():
    # Optional: Configure proxy settings
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = '10.10.1.10:3128'  # Replace with your proxy details
    proxy.ssl_proxy = '10.10.1.10:1080'

    options = Options()
    options.add_argument('--headless')  # Run in background without opening a browser window
    options.add_argument('--disable-gpu')
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
    # Uncomment the line below to enable proxy
    # options.proxy = proxy

    driver = webdriver.Chrome(options=options)
    return driver

def fetch_website_text(url):
    driver = setup_driver()
    try:
        driver.get(url)
        time.sleep(1)  # Let the page load completely, adjust the timing based on network speed and page complexity
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        text = ' '.join(soup.stripped_strings)
        return text
    except Exception as e:
        print(f"Error during scraping: {e}")
        return None
    finally:
        driver.quit()

# Example usage
#url = "https://www.bhphotovideo.com/c/product/1762582-REG/lenovo_82x70005us_15_6_ideapad_slim_3.html/fci/35801"
#url = "https://www.braceability.com/products/plus-size-knee-sleeve"
#url = "https://www.amazon.com/Cravings-Chrissy-Teigen-Stainless-Included/dp/B0D2JLG46R?pd_rd_w=3N4R0&content-id=amzn1.sym.a0a34a17-d48e-482a-9742-bc324f908aee&pf_rd_p=a0a34a17-d48e-482a-9742-bc324f908aee&pf_rd_r=JHG27MTDWB45DYQT2J1S&pd_rd_wg=os96W&pd_rd_r=984efef7-8edc-45b8-a19a-e25a290d3bf7&pd_rd_i=B0D2JLG46R&ref_=NewHome_B0D2JLG46R"
#text_content = fetch_website_text(url)
#if text_content:
#    print("Fetched Text Content:", text_content)  # Print the first 500 characters
#else:
#    print("Failed to fetch text content.")

