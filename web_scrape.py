from collections import defaultdict
from bs4 import BeautifulSoup
from selenium import webdriver

dr = webdriver.Chrome()
product_handle_list = []
product_tags_list = []
product_names = []
base_url = "https://www.braceability.com/collections/all?page="
prod_url = "https://www.braceability.com/products/"
for i in range(1, 5):
    num = i
    url = base_url + str(num)
    dr.get(url)
    bs = BeautifulSoup(dr.page_source,"lxml")

    # Find all div elements
    divs = bs.find_all('div')

    # Extract and print class names
    for div in divs:
        product_handle = div.get('data-product-handle')
        product_tags = div.get('data-limoniapps-discountninja-product-tags')
        
        if product_handle:
            # print('Product handle:', product_handle)
            product_handle_list.append(product_handle)
            # print('Tags: ', product_tags)
            product_tags_list.append(product_tags)

    # Find all overview key features
    features = bs.find_all('div', {'class': 'grid-product__title grid-product__title--heading'})
    feature_texts = [feature.get_text() for feature in features]
    product_names.extend(feature_texts)

# print("Overview Key Features:", feature_texts)

product_desc = {}

for i in range(len(product_names)):
    product_names[i] = product_names[i].strip()
    """
    url2 = prod_url+product_handle_list[i]
    dr.get(url2)
    bs2 = BeautifulSoup(dr.page_source,"lxml")
    div = bs2.find('div', class_='300')
    if div:
        h3 = div.find('h3')
        if h3:
            h3_text = h3.get_text()
    """
    product_desc[product_names[i]] = {"handle": product_handle_list[i], "tag": product_tags_list[i]}

print(product_desc)
