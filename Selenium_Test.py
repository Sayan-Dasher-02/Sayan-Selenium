from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Open Amazon and print all category names
driver.get("https://www.amazon.in/")
sleep(5)
a = driver.find_elements("id", "nav-main")
for i in a:
    print(i.text)

# Print top 10 movie names from IMDB Top 250
driver.get("https://www.imdb.com/chart/top/")
a = driver.find_elements("xpath", "//h3[contains(@class,'ipc-title__text')]")
for i in range(1, 11):
    print(i, a[i].text)

# Count all images on amazon
driver.get("https://www.amazon.in/")
sleep(4)
a=driver.find_elements("tag name", "img")
print(len(a))

# Open the site and target first dropdown in that page and select first option
driver.get("https://demoqa.com/select-menu")
driver.find_element(By.ID, "withOptGroup").click()
sleep(2)
driver.find_element("xpath", "//div[text()='Group 1, option 1']").click()

# Print All Links in amazon Page
driver.get("https://www.amazon.in/")
sleep(5)
a = driver.find_elements(By.TAG_NAME, "a")
for i in a:
    print(i.get_attribute("href"))

# Print Auto Suggestions of any site
driver.get("https://www.amazon.in/")
driver.find_element("id", "twotabsearchtextbox").send_keys("samsung")
sleep(3)
a = driver.find_elements("xpath", "//div[@class='s-suggestion-container']")
for i in a:
    print(i.text)

# From the “Accounts & Lists” section on the Amazon homepage, select the “Your Wish List” option.
driver.get("https://www.amazon.in/")
sleep(3)
a = driver.find_element("id", "nav-link-accountList")
o = ActionChains(driver)
o.move_to_element(a).perform()
sleep(2)
driver.find_element(By.LINK_TEXT, "Your Wish List").click()

# Access the content displayed inside the embedded page and print the heading text visible inside it.
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
driver.switch_to.frame("iframeResult")
driver.switch_to.frame(0)
a = driver.find_element(By.TAG_NAME, "h1").text
print(a)

# Search Laptop and print all product titles.
driver.get("https://www.amazon.in/")
sleep(5)
a = driver.find_element("id", "twotabsearchtextbox")
a.send_keys("Laptop")
a.send_keys(Keys.ENTER)
sleep(3)
a = driver.find_elements("xpath", "//h2//span")
for i in a:
    print(i.text)

sleep(5)
driver.quit()
