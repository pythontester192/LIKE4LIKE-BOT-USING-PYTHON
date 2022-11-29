from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AMFBot:
    def __init__(self, like4like_user, like4likepwd, twitter_user, twitter_pwd):
        self.like4like_user = like4like_user
        self.like4likepwd = like4likepwd
        self.twitter_user = twitter_user
        self.twitter_pwd = twitter_pwd
        self.options = Options()
        self.options.add_argument("--lang=en")
        self.bot = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=self.options)
    
    def open(self):
        bot = self.bot
        bot.maximize_window()
        bot.get("https://www.like4like.org/login/")
        usuario = bot.find_element_by_name("username")
        senha = bot.find_element_by_name("password")
        usuario.clear()
        senha.clear()
        usuario.send_keys(self.like4like_user)
        senha.send_keys(self.like4likepwd)
        bot.find_element_by_xpath('//*[@id="login"]/fieldset/table/tbody/tr[8]/td/span').click()
        time.sleep(5)
        ed.twtlk()
    
    def twtlk(self):
        bot = self.bot
        bot.get("https://www.like4like.org/free-twitter-followers.php")
        time.sleep(5)
        bot.find_element_by_css_selector("a[class^='cursor earn_pages_button profile_view_img']").click()
        time.sleep(2)
        bot.switch_to_window(bot.window_handles[1])
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
                bot.find_element_by_xpath('//div[@role="button"]//span[text()="Next"]').click()
                time.sleep(3)
                senha = bot.find_element_by_xpath("//input[@type='password']")
                senha.send_keys(self.twitter_pwd)
                bot.find_element_by_xpath('//div[@role="button" and @data-testid="LoginForm_Login_Button"]').click()
                follow = WebDriverWait(bot, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@role="button" and @data-testid="confirmationSheetConfirm"]'))
                )
                if follow.is_displayed():
                    follow.click()
                time.sleep(5)
            else:
                follow = bot.find_element_by_xpath('//div[@role="button" and @data-testid="confirmationSheetConfirm"]')
                if follow.is_displayed():
                    follow.click()
                time.sleep(5)

        except bot.NoSuchElementException:
            bot.close()
            bot.switch_to_window(bot.window_handles[0])
            time.sleep(5)
            bot.get("https://www.like4like.org/free-twitter-followers.php")
            ed.twttwo()
        
        #window
        bot.close()
        bot.switch_to_window(bot.window_handles[0])
        time.sleep(3)
        ed.twttwo()
    
    def twttwo(self):
        bot = self.bot
        confirm = bot.find_element_by_css_selector("a[class^='cursor pulse-checkBox']")
        if confirm.is_displayed():
            confirm.click()
            time.sleep(3)
            bot.find_element_by_css_selector("a[class^='cursor earn_pages_button profile_view_img']").click()
            bot.switch_to_window(bot.window_handles[1])
            #window
        else:
            bot.find_element_by_css_selector("a[class^='cursor earn_pages_button profile_view_img']").click()
            bot.switch_to_window(bot.window_handles[1])
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
            bot.switch_to_window(bot.window_handles[0])
            time.sleep(3)
            bot.get("https://www.like4like.org/free-twitter-followers.php")
            ed.twttwo()

        #window
        bot.close()
        bot.switch_to_window(bot.window_handles[0])
        time.sleep(3)
        ed.twttwo()


ed = AMFBot('like4like_user', 'like4likepwd', 'twitter_user', 'twitter_pwd')
ed.open()
