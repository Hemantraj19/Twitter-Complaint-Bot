from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 100
PROMISED_UP = 100
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""

internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
internet_speed.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)


