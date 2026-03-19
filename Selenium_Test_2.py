from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
import os

o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)
driver.implicitly_wait(10)

# Question 1
driver.get("https://demowebshop.tricentis.com")
sleep(3)
driver.find_element(By.LINK_TEXT,"Books").click()
sleep(2)
driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
sleep(2)
driver.find_element(By.LINK_TEXT,"Shopping cart").click()
sleep(2)
product=driver.find_element(By.XPATH,"//td[@class='product']/a")
print("Product is present in cart" if product.is_displayed() else "Product not found")

# Question 2
driver.get("https://demowebshop.tricentis.com")
sleep(2)
driver.find_element(By.LINK_TEXT, "Electronics").click()
sleep(2)
driver.find_element(By.XPATH, "(//a[contains(text(),'Cell phones')])[4]").click()

# Question 3
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
sleep(2)
driver.find_element(By.XPATH, "//button[text()='Start']").click()
sleep(2)
hello = wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Hello World!']")))
print(hello.text)

# Question 4
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
sleep(2)
driver.find_element(By.XPATH, "//button[text()='Remove']").click()
sleep(2)
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']")))
add_button.click()

# Question 5
driver.get("https://demoqa.com/select-menu")
sleep(2)
driver.find_element(By.ID, "withOptGroup").click()
sleep(2)
driver.find_element(By.XPATH, "//div[text()='Group 2, option 1']").click()
sleep(2)
selected = driver.find_element(By.XPATH,"//div[@id='withOptGroup']//div[contains(@class,'singleValue')]").text
print("Selected:", selected)

# Question 6
driver.get("https://demoqa.com/select-menu")
sleep(2)
multi = Select(driver.find_element(By.ID, "cars"))
multi.select_by_visible_text("Volvo")
multi.select_by_visible_text("Saab")
multi.select_by_visible_text("Opel")
sleep(2)
selected_options = [opt.text for opt in multi.all_selected_options]
print("Selected options:", selected_options)

# Question 7
driver.get("https://demoqa.com/menu/")
sleep(2)
main_item_2 = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
sub_sub_list = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
sub_sub_item_1 = driver.find_element(By.XPATH, "//a[text()='Sub Sub Item 1']")
sleep(2)
actions.move_to_element(main_item_2).perform()
actions.move_to_element(sub_sub_list).perform()
actions.click(sub_sub_item_1).perform()

# Question 8
driver.get("https://demoqa.com/droppable")
sleep(2)
source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")
sleep(2)
ActionChains(driver).drag_and_drop(source, target).perform()
sleep(2)
result = driver.find_element(By.ID, "droppable").text
print("Drop result:", result)

# Question 9
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
sleep(2)
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
sleep(2)
alert = driver.switch_to.alert
alert.accept()
sleep(2)
result = driver.find_element(By.ID, "result").text
print(result)

# Question 10
driver.get("https://the-internet.herokuapp.com/upload")
sleep(2)
file_path = r"C:\Desktop\Art of Giving.pdf"
sleep(2)
driver.find_element(By.ID, "file-upload").send_keys(file_path)
driver.find_element(By.ID, "file-submit").click()
sleep(2)
uploaded_file = driver.find_element(By.ID, "uploaded-files").text
print("Uploaded file:", uploaded_file)

# Question 11
driver.get("https://the-internet.herokuapp.com/download")
sleep(2)
file = driver.find_element("xpath", "//a[text()='testfile1.pdf']")
file_name = file.text
file.click()
sleep(5)
download_path = os.path.join(os.path.expanduser("~"), "Downloads")
file_path = os.path.join(download_path, file_name)
if os.path.exists(file_path):
    print("Downloaded:", file_name)
else:
    print("Download failed")

# Question 12
driver.get("https://demowebshop.tricentis.com")
sleep(2)
driver.find_element(By.LINK_TEXT, "Books").click()
sleep(2)
books = driver.find_elements(By.CSS_SELECTOR, ".product-item")
sleep(2)
for i in range(2):
    driver.find_elements("xpath", "//input[@value='Add to cart']")[i].click()
    sleep(2)
driver.find_element(By.LINK_TEXT, "Shopping cart").click()
sleep(2)
cart_items = driver.find_elements(By.CSS_SELECTOR, "tr.cart-item-row")
print("Total products:", len(cart_items))

# Question 13
driver.get("https://demowebshop.tricentis.com")
sleep(2)
driver.find_element(By.LINK_TEXT, "Books").click()
sleep(2)
books = driver.find_elements(By.CSS_SELECTOR, ".product-item")
for i in range(len(books)):
    books = driver.find_elements(By.CSS_SELECTOR, ".product-item")
    price = books[i].find_element(By.CSS_SELECTOR, ".actual-price").text
    price = float(price.replace("$", "").strip())
    if price < 20:
        title = books[i].find_element(By.CSS_SELECTOR, "h2.product-title").text
        buttons = driver.find_elements(By.XPATH, "//input[@value='Add to cart']")
        buttons[i].click()
        print("Added:", title, "| Price:", price)
        sleep(2)
        break

sleep(5)
driver.quit()