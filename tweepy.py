import tweepy
from datetime import datetime, timedelta 
import time 

consumer_key = '************'
consumer_secret = '*********'
access_token = '*******************'
access_token_secret = '****'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


def tweetar_mensagem(mensagem):
    api.update_status(status=mensagem)
    
while True:
    agora = datetime.now()
    if agora.hour == 12 and agora.minute == 0:
        tweetar_mensagem("Este é um tweet programado!")
        time.sleep(60)
    time.sleep(30)