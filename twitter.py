from twitter_scraper import *
import seaborn as sb

trends = get_trends()
data = dict()
print(trends)

i = 0
while i < len(trends):
    k = 0
    try:
        for tweet in get_tweets(trends[i], pages=1):
            print(tweet['tweetId'])
            k += 1
            data[trends[i]] = k
            print(data)
    except:
        print(data)
        print('error occured')
        break
    i += 1
