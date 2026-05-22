from selenium import webdriver


class Browser:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def close(self):
        self.driver.quit()
