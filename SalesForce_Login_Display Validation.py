from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

driver.get("https://login.salesforce.com/")
driver.title
print(driver.title)
driver.maximize_window()

usernameObtained = (driver.find_element_by_css_selector("div[id='usernamegroup'] label")).text
usernameExpected = "Username"
assert usernameObtained == usernameExpected , "Username Validation Failed"
print ("Username Validation passed")

passwordObtained = (driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)")).text
passwordExpected = "Password"
assert passwordObtained == passwordExpected , "Password Validation Failed"
print ("Password Validation passed")

remembermeObtained = (driver.find_element_by_xpath("//form[@name='login']/div[3]/label")).text
remembermeExpected = "Remember me"
assert remembermeObtained == remembermeExpected , "Remember me Validation Failed"
print ("Remember me Validation passed")

forgotpwdObtained = (driver.find_element_by_xpath("//div[@id='theloginform']/div/a[1]")).text
forgotpwdExpected = "Forgot Your Password?"
assert forgotpwdObtained == forgotpwdExpected , "Forgot password Validation Failed"
print ("Forgot password Validation passed")

custdomainObtained = (driver.find_element_by_xpath("//div[@id='theloginform']/div/a[2]")).text
customdomainExpected = "Use Custom Domain"
assert custdomainObtained == customdomainExpected , "Custom domain Validation Failed"
print ("Custom domain Validation passed")

driver.quit()