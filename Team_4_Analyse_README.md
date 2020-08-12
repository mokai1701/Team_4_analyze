Readme Team_4_ Analyse_Predict

The repository contains 7 functions that make use of Eskom data and Twitter data. 
The Eskom data is stored in a dataframe named ebp_df, and the twitter data is stored as a dataframe named twitter_df. 
More information stored in the form of lists and dictionaries has been made available to use within the functions as variables as per the requirement of each function. 
Below is a description of the comprehensive use of each function.

Function 1

Function 1 makes use of the ‘ebd_df’ and takes in a list as input to calculate the mean, median, variance as var, standard deviation as std, minimum and  the maximum. 
It returns a dictionary as output. Below are the steps followed to define and call function 1:
Numpy and Pandas are imported as np and pd respectively.
Define a function called ‘dictionary_of_metrics’ that takes in a parameter called ‘items’.
From the ebp_df data frame, create a list of items by converting a data series from type(float) to type(list).
Convert the items list into a numpy array to be able to calculate the above mentioned metrics, by using the:
.mean(), .median(), .var(ddof = 1), .std(ddof = 1), . min(), .max() numpy functions.
The ddof parameter is used in the variance and standard deviation to make sure they are not biased.
Create a dictionary called ‘metrics_dictionary’ that takes in the keys: ‘mean’, ‘median’, ‘var’, ‘std’, ‘min’, ‘max’,
and the calculation from the numpy array as the corresponding values.
Return the dictionary as output.
When called in a new cell, the function returns a dictionary.

Function 6

Function 6 makes use of the ‘twitter_df’ data frame and takes in a data frame as input. 
The ‘Tweets’ column is then extracted from the data frame and will be used to return another column called ‘Split Tweets’ that will split the words in the ‘Tweets’ data frame. 
Below are the steps followed to define and call function 6:
Pandas has already been previously imported as pd.
Define a function named ‘word_splitter’ that takes in a parameter called ‘df’.
The ‘Tweets’ column is then extracted from the dataframe and stored as a data series.
Create a variable named ‘tweets_dataseries_lower’, that stores the strings converted to lowercase from the data series using the pandas.Series.str.lower() method.
Create a variable named ‘tweets_dataseries_split’, that stores the split lowercase strings from the previous step using the pandas.Series.str.split() method.
Update the data frame ‘df’ with a column named, ‘Split Tweets’ that uses the ‘tweets_dataseries_split’ variable that contains the lowercase, split strings.
Return df as output.
When called in a new cell, the function returns a modified dataframe with a new column called ‘Split Tweets’.
