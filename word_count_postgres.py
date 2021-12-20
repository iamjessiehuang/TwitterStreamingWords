from datetime import datetime

#current_time = datetime.now().replace(microsecond=0,second=0) 
current_time = "2021-12-04 22:26:00" # FOR TESTING PURPOSES 
import psycopg2
import argparse
from datetime import datetime
import time
connection = psycopg2.connect("dbname=postgres user=parallels")
cursor = connection.cursor()
parser = argparse.ArgumentParser() 
parser.add_argument('--word',type=str,nargs='*',help='please type any word or phrase')
args = parser.parse_args()

word_search = args.word

if __name__ == '__main__':
	if args.word == None or args.word==[]:
		print('Please input the word or phrase')
	else:
		word_search = word_search[0]
		word_count = """select count(*) from words WHERE words = %s and time = %s;"""
		values = (word_search, current_time)
		cursor.execute(word_count,values)
		connection.commit()
		result = cursor.fetchone()
		print(result[0])
	##where word = %s and time=%s
	
	
#----------------------------------------------------

# Import the library
#import argparse

# Create the parser
#parser = argparse.ArgumentParser()

# Add an argument
#parser.add_argument('--word', type=str, required=True)

# Parse the argument
#args = parser.parse_args()
# Print "Hello" + the user input argument
#print('To search the following word in the text file: ', args.word)

#count = 0;  
#words = []; 
       
#Opens a file in read mode  
#file = open("tweets.txt", "r")  

#for line in file:  
#	#Splits each line into words  
#	string = line.lower().replace(',','').replace('.','').split(" ");  
#        #Adding all words generated in previous step into words  
#	for s in string: 
#		words.append(s);

		  
#for i in range(0, len(words)):
#	if(words[i] == args.word):  
#		count = count +1;
#		i = i+1;
#	else:
#		i = i+1;  
#print("Count of the word ", args.word+ " is", count)
#print(words[2])
#print(args.word)
#print(len(words))	
#file.close();           
 











