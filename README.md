# Using Twitter API to parse the words and phrases and count their frequencies
HOW TO RUN CODE  
1 - Have the tweets.txt in the same folder as server.py, vocabulary_size.py, and word_count.py.  
2 - Pip-install all of the libraries we use in server.py as well as running “python -m spacy download en_core_web_sm” within the Linux VM.  
    Import twitter, argparse, spacy, json, re, time  
    From datetime import datetime  
    Apply a developer account on twitter and acquire the consumer key and access token key  
3 - While running server.py in the Linux VM, make sure to eventually hit control Z (PC) or command Z (Mac) to stop the continuous stream of tweets.  
    server.py calls the Twitter API, creating a continuous stream of tweets, where vocabulary_size.py and word_count.py are just reading from a predetermined tweets.txt file.  
4 - Adjust the path in the line 33 in server.py to make sure it is representative of your local virtual machine.  
