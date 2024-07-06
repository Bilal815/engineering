import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def next_page(total_pages, pagination_div):
    # Loop through the total pages
    for page_num in range(1, int(total_pages) - 1):
        # Select the button within pagination div
        try:
            next_button = WebDriverWait(pagination_div, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@class="next"]'))
            )
            sleep(7)
            # Scroll to the next button
            driver.execute_script("arguments[0].scrollIntoView();", next_button)
                
            sleep(7)
            # Click the next button using JavaScript
            driver.execute_script("arguments[0].click();", next_button)
            next_button.click()
        except Exception as e:
            print("Error:", e)



while True:
    driver = webdriver.Firefox()
    driver.get("https://www.geekbuying.com/searchword/laptop/")
    driver.implicitly_wait(10)

    # selecting grid with all the product divs within it
    select_grid = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.gridView')))

    product_divs_list = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.searchResultItem')))

    # Scroll into view the last prod div
    driver.execute_script("arguments[0].scrollIntoView();", product_divs_list[-1])
    print(len(product_divs_list))
    
    # looping through every product div to get data
    for prod_div in product_divs_list:
        print(prod_div)
        name = WebDriverWait(prod_div, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.pro_title'))).text
        price_div = WebDriverWait(prod_div, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.price')))
        price = WebDriverWait(price_div, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.list-price'))).text
        review_div = WebDriverWait(prod_div, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.review')))
        review_num = WebDriverWait(review_div, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.review_num'))).text
        print('name', name)
        print('price', price)
        print('review_num', review_num)
        break


    # Wait until the overlaying element (<p>) disappears
    WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.XPATH, '//p')))

    # Now, locate and click the next button and total pages
    pagination_div = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pagination"]')))

    # Locating total pages by selecting the last a tag in the pagination_div
    total_pages_element = WebDriverWait(pagination_div, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="pagenumber"][last()]'))
    )
    total_pages = total_pages_element.text
    print('total_pages', total_pages)

    # Scroll to the next page
    #next_page(total_pages, pagination_div)
    driver.quit()

driver.quit()