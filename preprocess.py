import pandas as pd        

def tweet_precossess(tweets):
    """
    Splits user and their tweet into two columns of a dataframe.

    Args: 
        tweets dataframe containing 1 column. Each cell values pattern : '@user_id : tweet'
    Returns: 
        dataframe with 2 columns: 
             1.'user_id'(str) of tweet 
             2.'tweet_content' (str)
    """   

    #get all user_ids in a list
    user_id = [tweets['Tweets'][i].split(":",1)[0] for i in range(len(tweets['Tweets']))]

    #get all tweets in a list
    tweet_content = [tweets['Tweets'][i].split(":",1)[1] for i in range(len(tweets['Tweets']))]
    
    #convert all user_ids list and their tweets into columns of a dataframe. 
    df = pd.DataFrame({"user_id":user_id, "tweet_content": tweet_content})


    return df  

