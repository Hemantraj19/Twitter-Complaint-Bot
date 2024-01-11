import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.wait = WebDriverWait(self.driver, 10)
        self.down = 0
        self.up = 0
        self.element = "None"

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, "a span.start-text")
        go_button.click()
        indicator = "NaN"
        while indicator == "NaN":
            indicator = self.driver.find_element(By.CSS_SELECTOR, "div span.upload-speed").get_attribute(
                "data-upload-status-value")

        self.down = self.driver.find_element(By.CSS_SELECTOR, "div span.download-speed").text
        self.up = self.driver.find_element(By.CSS_SELECTOR, "div span.upload-speed").text

        print(self.down)
        print(self.up)
        self.driver.quit()

    def login_twitter(self, email, password):
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        email_entry = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        # email_entry.click()
        email_entry.send_keys(email)

        time.sleep(1)
        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()

        time.sleep(5)
        password_entry = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        # password_entry.click()
        password_entry.send_keys(password)

        final_login_button = self.driver.find_element(By.XPATH,
                                                      '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        final_login_button.click()
        time.sleep(5)

    def tweet_at_provider(self, email, password):
        self.login_twitter(email, password)
        message = f"Hey Internet Provider why is my internet speed {self.down} down / {self.up} up when i pay for 150 up / 150 down"
        text_box = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        text_box.send_keys(message)
        post_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        post_button.click()
