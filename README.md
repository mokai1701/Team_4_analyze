# Team 4 analyze package
this is a python package about analyzing metrics for eskom data

# Functions In this Packages
This package contains  7 functions that can be imported to do data analysis
and they make use of numpy and pandas

### function 1 dictionary of metrics
this function calculates the mean, median, variance, standard deviation, the minimum value and maximum value of a numpy array from a list of float values
and returns a dictionary of the aforementioned metrics

### function 2 summary statistics
this function takes an input of list of float numbers and
returns a five number summary statistics about that list using numpy

### function 3 date parser
This function takes input of a list of these datetime strings formatted as 'yyyy-mm-dd hh:mm:ss' and returns only the date in 'yyyy-mm-dd' format.
### function 4 extract municipality hashtags
This function takes a pandas twitter dataFrame and extracts municipality mentions and adds them to a new column called municipality and also extracts hashtags in the Tweets series and adds them to a new column called hashtags for each and every tweet row

### function 5 number of tweets per day
This is a function which takes a pandas dataframe as input of number of tweets per day and converts to new pandas dataframe into a new dataframe specified by the format yyyy-mm-dd

### function 6 word splitter
This function splits a dataseries from a dataframe into a new column of split words from a tweet

### functionm 7 stop words remover
The function takes a pandas dataframe of tweets that includes stop words as input and returns a modified dataframe without the stop words

# How to install this package
this package can only be installed from github as of yet
but you can install it by typing

`pip install git+https://github.com/mokai1701/Team_4_analyze.git `
in your command line. And make sure you have pip installed first

# How to Use this package
To use this package you have to import it into your python file or notebook by typing the following code
```
import team_4_analyze_package as t4p
```
and start using the functions or methods as

`
t4p.dictionary_of_metrics(list)
` 
for the dictionary of metrics 
and 
`
t4p.five_num_summary(list)
`
for the five number summary dictionary
and
`
t4p.date_parser(dates)
`
for a parsed date time strings to date format strings list
and
`
t4p.extract_municipality_hashtags(df)
`
for extracting municipality hashtag extractor
and
`
t4p.number_of_tweets_per_day(df)
`
for extracting the number of tweets per day
and
`
t4p.word_splitter(df)
`
for splitting / tokenizing the tweets
and 
`
t4p.stop_words_remover(df)
`
for removing stop words from a tweet