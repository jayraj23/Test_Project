from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://login.salesforce.com/")
driver.title  # title of the webpage
print(driver.title)

driver.maximize_window()
driver.find_element_by_link_text("Forgot Your Password?").click()

driver.title
print(driver.title)
driver.find_element_by_id("un").send_keys("Jayanthi")
driver.find_element_by_id("continue").click()
assert "Verify that your username is an email address" in "We can’t find a username that matches what you entered. Verify that your username is an email address (for example, username@company.com)","Validation Failed"

print("Validation passed")
driver.quit()