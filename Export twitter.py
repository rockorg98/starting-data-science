import tweepy 
from textblob import TextBlob
import csv

consumer_key='KH9P3w4ClSzk3OUmadYQ28DU8'
consumer_secret='d9E26bpZsmf78z6ldi5aqWhZHZAQbHH5MgRB2IjMzGdpkdnhHE'

access_token='1175651094627672064-LRWcIsjQKFp4x8yW5QayxBmmrHnTlr'
access_token_secret='mXnx24Q6T3YgxrH2x5wTv5ToN5qR4pCakFML3Af5l7rDm'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets=api.search('Modi')
li=[]
with open('file.csv','w') as csvfile:
	fieldnames=['today_tweets']
	writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
	for tweet in public_tweets:
		print(tweet.text)
		analysis=TextBlob(tweet.text)
		if analysis.polarity>-1:
			writer.writerow({'today_tweets':tweet.text.encode("utf-8")})

		#chcp 65001
		#use this command before running the file