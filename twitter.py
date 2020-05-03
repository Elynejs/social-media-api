from twitter_scraper import *
import urllib.request
import seaborn as sb
import random

trends = get_trends()
data = dict()
print(trends)

def dl_img(url, name):
    path = f'./images/{name}.jpg'
    urllib.request.urlretrieve(url, path)


i = 0
while i < len(trends):
    for tweet in get_tweets(trends[i], pages=1):
        if len(tweet['entries']['photos']):
            j = 0
            while j < len(tweet['entries']['photos']):
                url = tweet['entries']['photos'][j]
                try:
                    t_id = tweet['tweetId']
                    randint = random.randint(0, 9999)
                    name = f'{t_id}{randint}'
                    dl_img(url, name)
                    print('image downloaded')
                except:
                    print('couldn\'t download image')
                j += 1
    i += 1
