"""
Program documentation:
    Goal:
        1. Suppose you have two files with the extension ".csv".
        2. One file contains  Twitter  tweets from different users, and the other file shows racial slurs.
        3. The purpose of this program is to identify and report the number of racist slurs and the level of profanity expression per user.
        4. The degree of profanity is indicated by the ratio of (the number of racial slurs-words in the tweet) to (the total number of words in the tweet) x 100.
    Arguments:
        1. A file in csv format that contains the Twitter handle and its tweets. 
        2. CSV file containing racial slurs to search for. 
    Requirement:
        1. This program requires the following libraries:
            a. Pandas
        2. The file containing the tweet must be a single column file containing the user's Twitter handle (posting the tweet) and the tweet itself. H. 
           Each line is in the format "@user_handle tweet".
"""

import pandas as pd 
import argparse
from preprocess import tweet_precossess
from clean_proccess import tweet_process
from profanity import profanity_scores


def get_params() -> dict:
    """
    Helps access the path of racial_slurs file and tweets files independent of any platform,
    on which the program runs. 
    Here argparse module is used.
    argparse module makes it easy to write user-friendly command-line interfaces.
    """
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--Black_Racial_Slurs_location', required=False, default="./Black_Racial_Slurs.csv")
    parser.add_argument('--tweets_location', required=False, default="./tweets_blm.csv")
    return vars(parser.parse_args())



def read_data_frame(path):
    """
    Args :
        Path of the files
    Returns:
        dataframe : containting the contents of the files    
    """
    data_df = pd.read_csv(path)
    return data_df
    


def main():
    """ All functions are called here for the analysis of tweets."""
    params = get_params()
    
    #get the path/location of tweets file
    tweets_path = params['tweets_location']

    #read tweets file
    tweets = read_data_frame(tweets_path)
    
    #get the path/location of the racial slurs file.
    racial_slurs_path = params['Black_Racial_Slurs_location']

    #read racial slur file.
    black_racial_slurs = read_data_frame(racial_slurs_path)
    
    #preprocess tweets : seperate user_id and passwords in 2 columns
    tweet_preprocessed = tweet_precossess(tweets)
    
    #process text_cleaning of tweets
    tweet_s = tweet_process(tweet_preprocessed)
    
    #get profanity scores for each user
    df = profanity_scores(tweet_s, black_racial_slurs, tweet_preprocessed)

    print(df)
    
    #creates a csv file with columns : 1. user_id 2. degree of profanity by the user_id.
    df.to_csv('degree_of_profanity.csv')

    



if __name__ == '__main__':
    main()

    



