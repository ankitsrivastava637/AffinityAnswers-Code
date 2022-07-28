import pandas as pd 

def profanity_scores(tweets, black_racial_slurs, tweet_preprocessed):
    """
    Args : 
        3 dataframes

    Result :
        a dataframe conatining 3 columns : user_id, degree_of_profanity, tweets

    """
      
    tweet_s = tweets['tweet_content']
    
    #get and convert all racial_slurs into lower case
    slurs = black_racial_slurs['Racial Words'].str.lower().tolist()
    
    tweets_profainity_score = []

    for i in range(len(tweet_s)):

        tweet = tweet_s[i].split()
       
        tweet_profainity_count = 0

        for j in range(len(tweet)):
            if tweet[j] in slurs:
                tweet_profainity_count += 1
        
        #profanity score for each tweet range : 0 to 100 (float value)
        tweets_profainity_degree = (tweet_profainity_count/len(tweet))*100

        #append profanity score for each tweet in a list
        tweets_profainity_score.append(tweets_profainity_degree)  

    profanity_df = pd.DataFrame({'user_id' : tweets['user_id'], 
                                 'degree_of_profanity' : tweets_profainity_score, 'tweets': tweet_preprocessed['tweet_content']})   

    return profanity_df







