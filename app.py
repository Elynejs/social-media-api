from twitter_scraper import *
import seaborn as sb

trends = get_trends()
data = dict()
print(trends)

i = 0
while i < len(trends):
    k = 0
    try:
        for tweet in get_tweets(trends[i]):
            k += 1
            data[i] = k
    except:
        continue
    i += 1
print(data)
