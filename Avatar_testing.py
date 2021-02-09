import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://www.roblox.com/avatarshop")
driver.maximize_window()

driver.find_element_by_link_text("Avatar Shop").click()

avatars = driver.find_elements_by_css_selector("div[class='item-card-name-link']")

for avatar in avatars:
    if avatar == "Big Sad Eyes":
        break
time.sleep(7)
driver.find_element_by_css_selector("div[title='Big Sad Eyes']").click()
driver.find_element_by_css_selector("div[class='action-button'] button").click()

