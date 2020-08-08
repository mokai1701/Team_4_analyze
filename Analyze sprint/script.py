import pandas as pd
import numpy as np


ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

ebp_df.head()


twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)
twitter_df.head()

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}

### START FUNCTION
def dictionary_of_metrics(items):
    '''Parameter:
            The function takes in a list as input
       Body:
            The list is converted to a numpy array
            Created a dictionary that has the items as keys,
            The corresponding values to the items are calculated from the numpy array
       Return:
            Returns a dictionary as output 
    '''
                                
    items_np = np.array(items)
    metrics_dictionary = {'mean' : round(items_np.mean(), 2), 
                         'median':round(np.median(items_np,axis = None), 2),
                         'var' : round(items_np.var(ddof = 1), 2),
                         'std' : round(items_np.std(ddof = 1), 2),
                         'min' : round(items_np.min(), 2),
                         'max' : round(items_np.max(), 2)}

    return metrics_dictionary
### END FUNCTION

### START FUNCTION
def five_num_summary(items):
    # your code here
    """
    this function takes an input of list of float numbers and
    returns a five number summary statistics about that list
    using numpy
    
    parameters:
        items: accepts a list of floating numbers
    Body:
        Calculates the maximum, median, minimum, quantile 1 of 25%
        quantile 3 of 75% using numpy methods
    return:
        Returns a dictionary of the summary statistics of the floating numberes list
    """
    maximum = np.max(items)
    median = np.median(items)
    minimum=np.min(items)
    q1 = np.quantile(items,q=0.25)
    q3 = np.quantile(items,q=0.75)
    return {
        'max':maximum,
        'median':median,
        'min':minimum,
        'q1':q1,
        'q3':q3
    }

### END FUNCTION

### START FUNCTION
def date_parser(dates):
    """
    function date parser
    parameter: List of date time strings dates
    
    body:
        splits the date time strings list into only date strings list
    return: 
         date strings list in date format.
    """
    parsed_dates =[ ]#create a list for storing the date that has been parsed
    for date in dates: #Loop through the dates input list
        parsed_dates.append(date.split(' ')[0]) # append the parsed dates into the parsed_dates list
    return parsed_dates #returning the parsed dates

### END FUNCTION
### START FUNCTION
def extract_municipality_hashtags(df):
    # your code here
    return


### START FUNCTION
def number_of_tweets_per_day(df):
    # your code here
"""Function which list number of tweets per day by converting pandas dataframe into a new dataframe specified by yyyy-mm-dd"""
  df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
  return df.groupby('Date').count()
### END FUNCTION

### END FUNCTION

### START FUNCTION

def word_splitter(df):
    '''
        Parameter: 
            The function takes in a dataframe as input.
        Body:
            A copy of the input is made locally in the function
            It extracts a data series and put the contents of the data series as lower case strings.
            The lower case strings are split into a new list called  'tweets_data_series_split'
            The list is placed into a data series called 'Split Tweets' that is then modified into
            the dataframe, and is displayed as a new column called 'Split Tweets'
        
        Return:
            The function returs a dataframe with a new column called 'Split Tweets'
    '''
    df = twitter_df.copy() 
    tweets_dataseries = df['Tweets'] 
    tweets_dataseries_lower = tweets_dataseries.str.lower() 
    tweets_dataseries_split = tweets_dataseries_lower.str.split()
    df['Split Tweets'] = tweets_dataseries_split 
    return df

### END FUNCTION

### START FUNCTION
def stop_words_remover(df):
    """ 
    Function Stop words remover 

    Args : 

        token_tweets : splits(tokenizes) the tweets within the dataframe
        stops : stop words in the tokenized list
        df[] : modifies the input dataframe
    
    Return :
        dataframe : tweets without stop words

    Egs (for specific rows) :

        >>> stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za']
        
    """
        

    token_tweets = df.Tweets.apply(lambda x: x.lower().split()) 
    stops = stop_words_dict['stopwords']
    df["Without Stop Words"] = token_tweets.apply(lambda x: [word for word in x if word not in stops ])
    return df

### END FUNCTION


if __name__ == "__main__":
    dictionary_of_metrics(gauteng)
    five_num_summary(gauteng)
    date_parser(dates[:3])
    extract_municipality_hashtags(twitter_df.copy())
    number_of_tweets_per_day(twitter_df.copy())
    word_splitter(twitter_df.copy())
    stop_words_remover(twitter_df.copy())