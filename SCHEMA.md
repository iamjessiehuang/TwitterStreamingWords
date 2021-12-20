TWEETS (Tweet_ID, Tweet_Text, Timestamp) #Tweet_ID is the primary key

WORDS (Word_ID, Word_Text, Tweet_ID@, Timestamp) #Word_Id is the primary key, Tweet_ID is the foreign key

The TWEETS table captures the Tweet_ID which separates each tweet apart from each other regardless of whether the text is the same or not. It also captures the timestamp that each of these unique tweets is tweeted.

The WORDS table then breaks apart the tweet text from each unique tweet in the TWEETS table into the words that make up the Tweet Text. Each of these words in assigned a unique Word_Id while capturing the Tweet_ID that it was pulled from and timestamp that it was tweeted.

From these tables we'll be able to write SQL code to calculate frequency of all words and frequency of unique words at a time t and the minute before time t. We'll also be able to write to code to determine the frequency of a specific word at time t and the minute before time t. SQL code will then takes these calculations and input them into the trendiness formula to output a trendiness score.
