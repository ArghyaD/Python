from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import extractIMDB
import Key
import Structure
from SentimentAnalysis import sentAnalysis
from PIL import Image

#consumer key, consumer secret, access token, access secret.
ckey = Key.ckey
csecret = Key.csecret
atoken = Key.atoken
asecret = Key.asecret

extractIMDB.extractData()
tweetList=[]
class listener(StreamListener):

    def __init__(self,api=None):
        self.num_t=0

    def on_data(self, data):
#Reading upto 10 tweets for each celebrity
#The limit number can increased/decreased according to conviniance
        if self.num_t<10:
            all_data = json.loads(data)
            tweet = all_data["text"].encode("utf-8")
            tweet = Structure.structure(tweet) # This removes the links in the tweet which are not
                                               # required for sentiment analysis
            tweetList.append(tweet)
            print self.num_t+1," : ",tweet
        else:
            twitterStream.disconnect()
        self.num_t += 1


    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


#Try this to check
"""twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Trump"])
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["USA"])
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ronaldo"])
"""
names = extractIMDB.name
tmp = []
for i in names:
    l = "".join(i.split(" "))
    tmp.append(l)
names.extend(tmp)
for i in range(10):
    print "Tweets for :", names[i]
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[names[i],names[i+10]])
    result = sentAnalysis(tweetList)
    print "Celebrity name: ", extractIMDB.name[i]
    print "Profession: ", extractIMDB.profession[i]
    print "Best Work: ", extractIMDB.best_work[i]
    if result == 1:
        print "Overall Sentiment is Positive! "
    elif result==-1:
        print "Overall Sentiment is Negative! "
    else:
        print "Overall Sentiment is Neutral! "
    print "Opening Celebrity image..... "
    img = Image.open(extractIMDB.name[i]+'.jpg')
    img.show()
    img.close()
