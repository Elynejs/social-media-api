from twitter_scraper import *
import GetOldTweets3 as got

trends = get_trends()
data = dict()
print(trends)

for i in trends:
    criteria = got.manager.TweetCriteria().setEmoji('unicode')\
                                          .setQuerySearch(i)\
                                          .setSince('2020-04-29')\
                                          .setMaxTweets(10)
    
    tweet = got.manager.TweetManager().getTweets(criteria)
    for k in tweet:
        print(k.username)
        data[i] = k.date

print(data)