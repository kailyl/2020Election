import GetOldTweets3 as got

def userInput():
	user = input("Select Tweets from Biden or Trump: ")
	return user

def tweets(user):
	if user == "trump":
		username = "realDonaldTrump"
		query = "Joe Biden"
	elif user == "biden":
		username = "JoeBiden"
		query = "Donald Trump"
	tweetCriteria = got.manager.TweetCriteria().setUsername(username).setQuerySearch(query).setMaxTweets(20)
	tweets = got.manager.TweetManager.getTweets(tweetCriteria)
	for tweet in tweets:
		print('\n' + str(tweet.date)+ '\n' + tweet.text + '\n')

def main():
	user = userInput().lower()
	if(user == "trump"):
		tweets(user)
	elif(user == "biden"):
		tweets(user)
	else:
		print("Type either Trump or Biden")
		main()

main()