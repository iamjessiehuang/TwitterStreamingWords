from datetime import datetime

#current_time = datetime.now().replace(microsecond=0,second=0) 
current_time = "2021-12-04 22:26:00" # FOR TESTING PURPOSES 
import psycopg2
import argparse
from datetime import datetime
import time
connection = psycopg2.connect("dbname=postgres user=parallels")
cursor = connection.cursor()
vocab_size = """select count(distinct words) from words WHERE time = %s;"""
#values = (vocab_size, current_time)
cursor.execute(vocab_size,(current_time,))

connection.commit()
result = cursor.fetchone()
print(result[0])


