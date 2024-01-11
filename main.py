from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 100
PROMISED_UP = 100
TWITTER_EMAIL = "captainmarvel.cm11@gmail.com"
TWITTER_PASSWORD = "u3G%L4R)Y-f?S,3"

internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
internet_speed.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASSWORD)


