import tweepy 
access_key ='1025563697622786048-1dtVpbxm8nvRl4QYimNkPxuPYRCzhv'
access_secret='GskrS6lZFpSk1A5injnEwARLaNfhU6VAnURhr9sVYMAdu'
consumer_key = 'ySnXmMkdA3OyhdYqfKepYTpIR'
consumer_secret = 'sU1wZGkukA2JzANEFd0EZZx2AGm04fMzGv1E9YmRmqegbuhJaL'
# Function to extract tweets 
def get_tweets(username,_size): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=_size
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j) 
  
        return tmp
  
  
'''# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("samsung")  '''