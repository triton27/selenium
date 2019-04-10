from selenium import webdriver

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get("https://github.com/triton27/selenium");
driver.save_screenshot('screen.png')
driver.close()
driver.quit()
