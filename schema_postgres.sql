--CREATE DATABASE postgres
--USE postgre;s




CREATE TABLE words(
word_text varchar(100), --we'd be able to compute frequency of words directly from count * or count distinct
count int, --this is the variable that displays the count of each word, we had issues being able to compute it
word_timestamp timestamp
);
