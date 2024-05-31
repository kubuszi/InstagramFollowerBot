from selenium import webdriver


SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
