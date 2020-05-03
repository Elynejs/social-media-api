from twitter_scraper import *
import urllib.request
import random
import fs

trends = get_trends()
search = input('Enter your desired search string :')
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
        i = 0
        while i < len(urls):
            f.write(f'{urls[i]}\n')
            i += 1

#i = 0
#while i < len(trends[i]):
try:
    for tweet in get_tweets(search):
        if len(tweet['entries']['photos']):
            j = 0
            while j < len(tweet['entries']['photos']):
                url = tweet['entries']['photos'][j]
                urls.append(url)
                if check_url(url):
                    try:
                        t_id = tweet['tweetId']
                        randint = random.randint(0, 9999)
                        name = f'{t_id}{randint}'
                        dl_img(url, name)
                        print('image downloaded')
                    except:
                        print('couldn\'t download image')
                else:
                    print('image already downloaded')
                j += 1
        else:
            print('no image found')
except ValueError:
    print('encountered a value error')
    #continue
    #break
#i += 1
append_url()
