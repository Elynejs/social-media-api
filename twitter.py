import twitter_scraper as t
import urllib.request

trends = t.get_trends()
pages_to_search = 10
ids = []

def dl_img(url, name):
    path = f'./images/{name}.jpg'
    urllib.request.urlretrieve(url, path)


for trend in trends:
    try:
        for i in range(1, pages_to_search):
            for tweet in t.get_tweets(trend, pages=i):
                if len(tweet['entries']['photos']):
                    t_id = tweet['tweetId']
                    if t_id not in ids:
                        ids.append(t_id)
                        for j in range(0, len(tweet['entries']['photos'])):
                            try:
                                url = tweet['entries']['photos'][j]
                                name = f'{trend}_{t_id}_{j}'
                                dl_img(url, name)
                                print('image downloaded')
                            except:
                                print('couldn\'t download image')
                    else:
                        print('image already downloaded')
                else:
                    print('no image found')
    except:
        trends.remove(trend)
        print(f'remove {trend} from trends because it caused an error')
