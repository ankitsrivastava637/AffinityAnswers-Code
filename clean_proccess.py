import pandas as pd  
import re 


def tweet_process(df):
    """
    Cleans tweets : Removes url links from each tweet,
    removes stopwords, removes punctuations from each tweet.

    Args:
        dataframe with 2 columns: 
             1.'user_id'(str) of tweet 
             2. 'tweet_content' (str)

    Returns:
        dataframe with 2 columns (after doing intented tasks of the function):
            1.'user_id'(str) of tweet 
            2.'tweet_content' (str)      

    """
    
    #empty list
    temp_tweet_content = []

    #loop to clean each tweet at a time
    for i in range(len(df['tweet_content'])):

        tweet = df['tweet_content'][i]  

        #remove https links in the tweet/URLs mixed up in any text
        tweet = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', tweet) 
        
        #remove punctuations in the tweet
        tweet = re.sub(r'[^\w\s]', '', tweet) 
        
        #convert each tweet to lowercase characters 
        tweet = tweet.lower()
        
        #remove stopwords
        tweet = remove_stopwords(tweet)
        
        #add each cleaned/processed tweet to list temp_tweet_content
        temp_tweet_content.append(tweet)

    #assign user_ids and cleaned/processed tweets into columns of a dataframe.
    df = pd.DataFrame({'user_id': df['user_id'], 'tweet_content': temp_tweet_content})  

    return df  

        

def remove_stopwords(tweet):
    """
    Args : 
        tweet of each user : string
    Return : 
        tweet of each user without stopword : string    
    """
    
    #splits the sentences into list of words 
    tweet_ls = tweet.split()
    
    #list of certain irrelevant words for analysis. 
    stopwords = {'a', 'the', 'is', 'are', 'as', 'an'}
    
    #exclude stop words from the list words
    resultwords  = [word for word in tweet_ls if word not in stopwords]

    #convert list of words into one sentence.
    tweet_s = ' '.join(resultwords)  
    
    return tweet_s        