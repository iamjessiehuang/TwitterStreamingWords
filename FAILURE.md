Failure 1 
"Exceeded connection limit for user" when running the python3 server.py code

Recovery Logic 1
Multiple team members applied for and created developer accounts to run the code with our own respective tokens and increase our connection attempts. A second solution was to wait 15 minutes before trying to run the code again. 

Failure 2 
After we got the tweetstream to work, we were not able to print the timestamps because deleted tweets were included in the tweetstream. 

Recovery Logic 2
Connected with Emaad to identify the problem and filter out the deleted tweets. He provided the code. 

Failure 3 
Initially, we were grabbing the wrong timestamp when trying to print tweets in the requested format.
Recovery: We looked up the dictionary keys to identify what could be used for 'timestamp'. We found "created_at",  which we then set to be the actual timestamp.

Recovery Logic 3
for tweet in tweets:
   print(tweet)
   print(tweet.keys())
  for tweet in tweets:
     if 'delete' in tweet.keys():
        continue    
     if tweet['lang'] == "en":
       tweet['text'] = clean_text(tweet['text'])
       date = datetime.strptime(tweet['created_at'],"%a %b %d %H:%M:%S +0000 %Y")
       date1 = date.strftime("%Y-%m-%d-%H-%M-%S")
       print(date1, tweet['text'])
       input = (date1, tweet['text'])
       writefile.write('%s, %s\n' % (date1, tweet['text']))
       
Failure 4 
Our original code of “dot split” to split up words for word count and vocabulary size was not working within Python. As a solution, we had to use the ‘Argparse’ code in the text file.

Recovery Logic 4
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--word', type=str)#, required=True)

	args = parser.parse_args()
	# Print "Hello" + the user input argument
	#words = []
	file = open("tweets.txt", "r")



