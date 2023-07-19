import tweepy
from textblob import textblob

#debe remplazar "TU_CONSUMER_KEY", "TU_CONSUMER_SECRET"....

consumer_key = "1Hve5wApr9gtvaBWyDlk1KEvj"
consumer_secret = "8hiv9EYkgbqQpJ7sztAPtjXAf6zUZMkaGP1u2XbewF8334QgJL"
access_token = "1681376775983464466-hNFb8hdVORURQ6HEda7cboCzc6Sa4g"
access_token_secret = "rLxF4GYaln8EK5zbKE14TBYmkUuTsOSe6Edz3MiHrIm7V"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 



#Puede personalizar los parámetros de búsqueda y ajustar el número de tweets a recopilar según sus necesidades. 
query = "deportes" 
tweet_count = 100  # Número de tweets a recopilar 

tweets = tweepy.Cursor(api.search_tweets, q=query, lang="es").items(tweet_count) 
#La polaridad de los tweets se determina según el valor de la polaridad devuelta por TextBlob: valores positivos indican sentimientos positivos, valores negativos indican sentimientos negativos, y valores cercanos a cero indican neutralidad. 


positive_count = 0 
negative_count = 0 
neutral_count = 0 

 

for tweet in tweets: 
    analysis = textblob(tweet.text) 
    sentiment = analysis.sentiment.polarity 
    if sentiment > 0: 
        positive_count += 1 
    elif sentiment < 0: 
        negative_count += 1 
    else: 
        neutral_count += 1 

total_count = positive_count + negative_count + neutral_count 

print("Total de tweets recopilados:", total_count) 

print("Tweets positivos:", positive_count) 

print("Tweets negativos:", negative_count) 

print("Tweets neutrales:", neutral_count) 
