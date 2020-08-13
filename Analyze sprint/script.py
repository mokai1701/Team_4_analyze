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


def dictionary_of_metrics(items):
  """
    The function calculates the mean, median,var,std,min,max of a numpy array from a list of values.

    Parameters
    -----------
    The function takes in a list of items as input.
        
    Returns
    -----------
    Returns a dictionary as output 
    """
                                
    items_np = np.array(items)
    metrics_dictionary = {'mean' : round(items_np.mean(), 2), 
                         'median':round(np.median(items_np), 2),
                         'var' : round(items_np.var(ddof = 1), 2),
                         'std' : round(items_np.std(ddof = 1), 2),
                         'min' : round(items_np.min(), 2),
                         'max' : round(items_np.max(), 2)}

    return metrics_dictionary


def five_num_summary(items):
    """
    this function takes an input of list of float numbers and
    returns a five number summary statistics about that list
    using numpy
    
    Parameters:
    -----------
    items: list
            A list of float numbers
    
    Return:
    -------
    dictionary: 
            A dictionary with all the summary statistics
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


### START FUNCTION
def date_parser(dates):
     """
    This function takes input of a list of these datetime strings formatted as 'yyyy-mm-dd hh:mm:ss' 
    and returns only the date in 'yyyy-mm-dd' format.
    
    Parameters:
    -----------
    dates: List of date time strings dates formatted as 'yyyy-mm-dd hh:mm:ss'.

    Returns
    -------
     date strings list in 'yyyy-mm-dd' format.
   
    """
    parsed_dates =[ ]
    for date in dates: 
        parsed_dates.append(date.split(' ')[0]) 
    return parsed_dates 
### END FUNCTION


def extract_municipality_hashtags(df):
    """
    This function takes a pandas twitter dataFrame and extracts municipality mentions
    and adds them to a new column called municipality
    and also extracts hashtags in the Tweets series and adds them to a new column called hashtags
    for each and every tweet row
    Parameters:
    -----------
  
    df: Pandas dataFrame
        The twitter dataframe containing tweets and dates
    
    Returns:
    --------
    
    df: Pandas dataFrame 
        A modified dataframe with added columns called municipality and hashtags
    """
    df['municipality'] = df['Tweets'].apply(lambda muni: [municipality for municipality in muni.split() if municipality.startswith('@')])
    df['municipality'] = df.index.to_series().map(mun_dict)
    Tweets = df['Tweets'].apply(lambda words: [word.lower() for word in words.split() if word.startswith('#')])
    df['hashtags'] = Tweets.apply(lambda hashtag: np.nan if len(hashtag)==0 else hashtag)
    return df

### START FUNCTION
def number_of_tweets_per_day(df):

  """Function which takes a pandas dataframe as input of number of tweets per day and converts to new pandas dataframe into a new dataframe specified by the format yyyy-mm-dd

  Parameters :
    
    Dataframe input converted to yyyy-mm-dd format
    Groups by format and counts number of tweets

  Return   :

    DataFrame(df) : number of tweets per day organised in new dataframe grouped by day for dates 2019-11-20 to 2019-11-29
  
  """


  df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d') #dataframe input converted to yyyy-mm-dd format
  new_df = df.groupby('Date').count() #groups by format and counts number of tweets
  return new_df
### END FUNCTION


### END FUNCTION



def word_splitter(df):
    """
    The function splits a dataseries from a dataframe into a new column.
        
    Parameters
    -----------
    The function takes in the dataframe 'df' as input.
    
    Returns
    ----------
    The function returns a dataframe with a new column called 'Split Tweets' as output.
    """
    df = twitter_df.copy() 
    tweets_dataseries = df['Tweets'] 
    tweets_dataseries_lower = tweets_dataseries.str.lower() 
    tweets_dataseries_split = tweets_dataseries_lower.str.split()
    df['Split Tweets'] = tweets_dataseries_split 
    return df




def stop_words_remover(df):    
    """ 
    The function takes a pandas dataframe of tweets that includes stop words as input and 
    returns a modified dataframe without the stop words 

    Parameters 
    ----------- 

        token_tweets : splits(tokenizes) the tweets within the dataframe
        stops : stop words in the tokenized list
        df[] : modifies the input dataframe
    
    Return 
    ----------
        df : a modified DataFrame of tweets without stop words
           
    """

    token_tweets = df.Tweets.apply(lambda x: x.lower().split()) 
    stops = stop_words_dict['stopwords']
    df["Without Stop Words"] = token_tweets.apply(lambda x: [word for word in x if word not in stops ])
    return df




if __name__ == "__main__":
    dictionary_of_metrics(gauteng)
    five_num_summary(gauteng)
    date_parser(dates[:3])
    extract_municipality_hashtags(twitter_df.copy())
    number_of_tweets_per_day(twitter_df.copy())
    word_splitter(twitter_df.copy())
    stop_words_remover(twitter_df.copy())