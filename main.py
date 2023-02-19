import csv
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Options for correct work driver
options = Options()
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-dev-shm-usage")

executable_path = Service("/home/unotuno/python/pythonProject/lamoda_parsing/chromedriver")
driver = webdriver.Chrome(service=executable_path, options=options)
driver.maximize_window()
driver.get("https://www.lamoda.by/catalogsearch/result/?q=%D0%BA%D1%80%D0%BE%D1%81%D1%81%D0%BE%D0%B2%D0%BA%D0%B8+nike"
           "+%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B8%D0%B5&submit=y&gender_section=men"
           )

# function return links of each product card that driver.get(link):
def start_pars():
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "x-product-card__link")))
        a = []
        products_info = driver.find_elements(By.CLASS_NAME, "x-product-card__pic-catalog")
        for x in products_info:
            a.append(x.get_attribute("href"))
        return (a)
    except Exception as ex:
        print(ex)


# empty list for dict with goods info (Price, Model, Rank, Link)
box_info = []

# function to get all needed data on the webpage
def data_pars(links):
    for link in links:
        box_for_data = dict()
        driver.get(link)
        # waiting while info container loaded
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "_stickyContainer_1l1jf_40"))
            )
        except NoSuchElementException:
            print("sorry time is over")

        box_for_data["Link"] = link

        try:
            product_price = driver.find_element(By.CLASS_NAME, "_price_11f1r_7").text
            box_for_data["Price"] = product_price
        # if price empty should write /null/ on csv file;
        except NoSuchElementException:
            box_for_data["Price"] = None

        try:
            product_model = driver.find_element(By.CLASS_NAME, "_modelName_fbl6x_22").text
            box_for_data["Model"] = product_model
        # if Model empty should write /null/ on csv file;
        except NoSuchElementException:
            box_for_data["Model"] = None

        try:
            product_rank = driver.find_element(By.CLASS_NAME, 'product-rating__count').text
            box_for_data["Rank"] = product_rank
        # if rank empty should write /null/ on csv file;
        except NoSuchElementException:
            box_for_data["Rank"] = None
        box_info.append(box_for_data)

def data_csv():
    columns = set(i for d in box_info for i in d)
            # create rows with goods data
    with open('out.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()  # Пишем заголовок
        for row in box_info:
            writer.writerow(row)


# let's go my sweetie.
if __name__ == "__main__":
    start_pars()
    links = start_pars()
    data_pars(links)
    data_csv()

