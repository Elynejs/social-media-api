from twitter_scraper import *
import urllib.request
import random

trends = get_trends()
pages_to_search = 10
urls = []

def dl_img(url, name):
    path = f'./images/{name}.jpg'
    urllib.request.urlretrieve(url, path)

def check_url(url):
    with open('twitter_img_url.txt', 'r+') as f:
        if url in f.read():
            f.close()
            return False
        else:
            f.close()
            return True

def append_url():
    with open('twitter_img_url.txt', 'w+') as f:
        x = 0
        while x < len(urls):
            f.write(f'{urls[i]}\n')
            x += 1

try:
    for m in range(0, len(trends)):
        for i in range(1, pages_to_search):
            for tweet in get_tweets(trends[m], pages=i):
                if len(tweet['entries']['photos']):
                    for j in range(0, len(tweet['entries']['photos'])):
                        url = tweet['entries']['photos'][j]
                        urls.append(url)
                        if check_url(url):
                            try:
                                t_id = tweet['tweetId']
                                if len(tweet['entries']['photos']):
                                    for l in range(0, len(tweet['entries']['photos'])):
                                        photo_number = l
                                        name = f'{t_id}_{photo_number}'
                                        dl_img(url, name)
                                        print('image downloaded')
                                else:
                                    name = f'{t_id}_1'
                                    dl_img(url, name)
                                    print('image downloaded')
                            except:
                                print('couldn\'t download image')
                        else:
                            print('image already downloaded')
                else:
                    print('no image found')
except:
    print('error occured')
append_url()
