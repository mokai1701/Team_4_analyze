# Team_4_analyze

This will show the package we're going to install has been packaged. moreover it allows for easy installation of the our python package.

# Functions 
Contains all the datafile imports and function definition for all our 7 functions

Function 7 :

    The function reduces the replication of code by removing english stop words from a tweet
    Essentially the stop word remover function inputs a panadas dataframe of tweets
    and outputs a modified dataframe that has removed the english stop words from a tweet 
    This is achieved by :
        1. tokeninizing the sentences 
        2. removing all stop words in the tokenised list 
        3. places the tokenised list in a column named "Without Stop Words"
        4. the defined function returns a modified dataframe

    The stopwords are defined in the stop_words_dict variable defined 


# Script.py
This is a script file which you use to call all our functions and imports for more effective use.

# Instruction
If you want to use our package you can type
pip install git+https://github.com/mokai1701/Team_4_analyze.git
