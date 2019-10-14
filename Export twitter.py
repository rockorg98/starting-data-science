# This file can be directly use to import tweets from twitter and pushing the tweets with some minimum polarity to a CSV file.
import tweepy 
from textblob import TextBlob
import csv

consumer_key='xxxx'
consumer_secret='yyyyy'

access_token='lllllll'
access_token_secret='mmmmmm'

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
